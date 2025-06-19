import torch

print("🔥 Testando GPU no Colab...")

if torch.cuda.is_available():
    print(f"✅ GPU disponível: {torch.cuda.get_device_name(0)}")
else:
    print("❌ GPU não disponível")

# Pequeno treino de exemplo
x = torch.randn(10000, 10000, device="cuda")
y = torch.matmul(x, x)
print("🔥 Operação na GPU feita com sucesso!")