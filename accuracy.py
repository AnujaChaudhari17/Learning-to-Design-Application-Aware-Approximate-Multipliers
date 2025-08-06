def train_and_evaluate():
    import torch
    import torch.nn as nn
    import torch.optim as optim
    import torchvision.transforms as transforms
    from torchvision.datasets import MNIST
    from torch.utils.data import DataLoader
    import torch.ao.quantization as quant
    import torchapprox.layers as tal
    from torchapprox.utils import wrap_quantizable, get_approx_modules
    import numpy as np
    import time
    import torch.nn.functional as F
    from torch.utils.data import DataLoader, Subset
    print("Checking for GPU availability...")
    # Check for GPU availability
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    # Define the custom CNN model
    print("Defining the custom CNN model...")
    class LeNet5(nn.Module):
        def __init__(self):
            super(LeNet5, self).__init__()
            self.conv1 = nn.Conv2d(in_channels=1, out_channels=6, kernel_size=5, stride=1, padding=2)  # Output: 28x28
            self.pool1 = nn.AvgPool2d(kernel_size=2, stride=2)  # Output: 14x14
            self.conv2 = nn.Conv2d(in_channels=6, out_channels=16, kernel_size=5, stride=1)  # Output: 10x10
            self.pool2 = nn.AvgPool2d(kernel_size=2, stride=2)  # Output: 5x5
            self.fc1 = nn.Linear(16 * 5 * 5, 120)  # Fully connected layer
            self.fc2 = nn.Linear(120, 84)
            self.fc3 = nn.Linear(84, 10)  # 10 output classes (digits 0-9)

        def forward(self, x):
            x = F.relu(self.conv1(x))
            x = self.pool1(x)
            x = F.relu(self.conv2(x))
            x = self.pool2(x)
            x = x.view(-1, 16 * 5 * 5)  # Flatten for FC layers
            x = F.relu(self.fc1(x))
            x = F.relu(self.fc2(x))
            x = self.fc3(x)  # No activation (CrossEntropyLoss includes softmax)
            return x
    # print("Initializing custom CNN model...")
    # Initialize the model
    model = LeNet5()
    model.to(device)
    # print("Model initialized successfully!")

    # print("Wrapping layers for quantization...")
    # Wrap layers for quantization
    wrap_quantizable(model)
    # print("Wrapping completed.")

    # print("Preparing the model for QAT...")
    # Prepare model for Quantization-Aware Training (QAT)
    quant.prepare_qat(model, tal.layer_mapping_dict(), inplace=True)
    # print("Model prepared for QAT.")

    # print("Preparing MNIST dataset...")
    # Set up the dataset and data loaders
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))  # Normalize to range [-1, 1]
    ])
    # train_dataset = MNIST(root='./data', train=True, download=True, transform=transform)
    test_dataset = MNIST(root='./data', train=False, download=True, transform=transform)
    # num_samples = 20000
    # indices = torch.randperm(len(train_dataset))[:num_samples]

    # Use Subset to create a smaller dataset
    # subset_train_dataset = Subset(train_dataset, indices)
    # train_loader = DataLoader(subset_train_dataset, batch_size=256 * 4, shuffle=True, pin_memory=True, num_workers=8)
    test_loader = DataLoader(test_dataset, batch_size=256 * 4 * 4, shuffle=False, pin_memory=True, num_workers=8)
    # print("Dataset and data loaders ready.")

    # print("Setting up the loss function and optimizer...")
    # Set up the loss function and optimizer
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    # print("Loss function and optimizer set up.")

    # Generate the Lookup Table (LUT) for approximate multiplication
    from temp import multiply2  # Import the multiply2 function from temp.py

    def apply_bias(value):
        return value if value < 128 else value - 256

    lut_size = 256
    lut = np.zeros((lut_size, lut_size), dtype=np.int16)

    for i in range(lut_size):
        for j in range(lut_size):
            x_biased = apply_bias(i)
            y_biased = apply_bias(j)
            product = multiply2(abs(x_biased * 2), abs(y_biased * 2))
            if (i >= 128 and j < 128) or (i < 128 and j >= 128):
                product = -product
            lut[i][j] = product / 4

    # Function to set approximate forward pass
    def set_approx_forward(model, lut):
        for name, module in get_approx_modules(model):
            if hasattr(module, 'approx_fwd'):
                module.lut = lut
                module.inference_mode = tal.InferenceMode.APPROXIMATE
                # print(f"Set approx_fwd with LUT for module: {name}")
            else:
                continue
                # print(f"Module {name} does not support approx_fwd.")

    # Switch to approximate multiplication mode
    set_approx_forward(model, lut)


    # Fine-tune the model with approximate multiplication
    
    #load the model - 
    model.load_state_dict(torch.load('lenet_mnist_final_CNN.pth'))

    # print("Validating the model...")
    # Validate the model
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for inputs, labels in test_loader:
            inputs, labels = inputs.to(device), labels.to(device)
            outputs = model(inputs)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    accuracy = 100 * correct / total
    # print(f"Validation complete. Accuracy on test set: {accuracy:.2f}%")
    
    return accuracy


# accuracy = train_and_evaluate()
# print(f"Final accuracy: {accuracy:.2f}%")
