# função para gerar amostras de dados numéricos

def data_sample(n: int) -> int:
    import numpy as np

    x = np.random.randn(n)
    y = np.random.randn(n)

    return x, y


x = data_sample(10)
y = data_sample(10)

print(f'x: {x}', f'y: {y}', sep='\n\n')