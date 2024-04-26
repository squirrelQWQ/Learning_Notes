def test_model(model, test_loader, criterion, device='cuda'):
    model.eval()  # 设置模型为评估模式
    test_loss = 0.0
    correct = 0
    total = 0
    TP = 0  # 真正例
    FP = 0  # 假正例
    FN = 0  # 假负例
    TN = 0  # 真负例

    with torch.no_grad():
        for inputs, labels in test_loader:
            inputs, labels = inputs.to(device), labels.to(device)
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            test_loss += loss.item()

            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
            TP += ((predicted == 1) & (labels == 1)).sum().item()
            FP += ((predicted == 1) & (labels == 0)).sum().item()
            FN += ((predicted == 0) & (labels == 1)).sum().item()
            TN += ((predicted == 0) & (labels == 0)).sum().item()

    precision = TP / (TP + FP) if (TP + FP) > 0 else 0
    recall = TP / (TP + FN) if (TP + FN) > 0 else 0
    F1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

    print(f"在验证集上的TP为：{TP}")
    print(f"在验证集上的FP为：{FP}")
    print(f"在验证集上的FN为：{FN}")
    print(f"在验证集上的TN为：{TN}")
    print(f"验证集损失为：{test_loss / len(test_loader)}")
    print(f'在验证集上的准确率为：{100 * correct / total}%')
    print(f'在验证集上的召回率为：{100 * recall}%')
    print(f'在验证集上的F1分数为：{F1}')