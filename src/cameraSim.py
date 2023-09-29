from datetime import datetime

def detections(detected):
    info = []
    for detection in detected:
        match detection:
            case 'caminhao':
                print('Caminhão detectado')
                placa = '"placa":"XXX-0000"'
                cor = '"cor":"amarelo"'
                condicaoEstrutural = '"condicaoEstrutural":"bom"'
                deformacoes = ['amassado_leve_porta_direita','rachadura_para_brisa']
                deformacoes = '"Deformações": ["'+'","'.join(deformacoes) + '"]'
                excessoDeCarga = False
                excessoDeCarga = '"ExcessoDeCarga":"False"'
                condicaoPneus = ['bom','bom','meia-vida','meia-vida']
                condicaoPneus = '"Condiçãopneus": ["'+'","'.join(condicaoPneus) + '"]'
                posicionamentoCelula = '"posicionamentoCelula":"centralizado"'
                tipoCarro = '"tipoCarro":"bitrem"'
                '''newInfo = {'placa':placa, 'cor':cor, 'condicaoEstrutural':condicaoEstrutural,'deformacoes':deformacoes,'excessoDeCarga':excessoDeCarga,'condicaoPneus':condicaoPneus,'posicionamentoCelula':posicionamentoCelula,'tipoCarro':tipoCarro}
                info.append(newInfo)'''
                name = './rawInfo/caminhao_'+datetime.now().strftime("%d%m%Y%H%M%S")+'.txt'
                f = open(name,'w',encoding='utf-8')
                f.write(placa+'\n'+cor+'\n'+condicaoEstrutural+'\n'+deformacoes+'\n'+excessoDeCarga+'\n'+condicaoPneus+'\n'+posicionamentoCelula+'\n'+tipoCarro)
                f.close()
                info.append(name)

            case 'pessoa':
                print('Pessoa detectada')
                status = '"status":"permitido"'
                '''newInfo = {'deteccaoExtra':'pessoa','status':status}
                info.append(newInfo)'''
                name = './rawInfo/extraDetec_'+datetime.now().strftime("%d%m%Y%H%M%S")+'.txt'
                f = open(name,'w', encoding='utf-8')
                f.write(status)
                f.close()
                info.append(name)

    return info


def simulator(detecting):
    if detecting:
        print("\n--CAMERA STARTED DETECTION--\n")
        detected = []
        detected.append('caminhao')
        detected.append('pessoa')
        return detections(detected)

        
    