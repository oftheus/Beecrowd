
while(1):

    x_l_0, y_l_0, x_l_1, y_l_1 = list(map(int, input().split()))
    x_r_0, y_r_0, x_r_1, y_r_1 = list(map(int, input().split()))

    # não precisamos ligar para a area de sobreposição
    # precisamos saber onde é o ponto mínimo em X e o ponto máximo em X para reterminar se eles se sobrepoem em x
    # y é analogo

    sobreproe_em_x = min(x_l_1, x_r_1) - max(x_l_0, x_r_0)

    sobreproe_em_y = min(y_l_1, y_r_1) - max(y_l_0, y_r_0)

    if (sobreproe_em_x >= 0 and sobreproe_em_y >= 0):
        print(1)
    else:
        print(0)

    print()