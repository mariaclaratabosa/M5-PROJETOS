from datetime import datetime, timedelta

STR_FORMATACAO = '%d/%m/%y %H:%M:%S'

exame_realizado_em = datetime.now()

print(exame_realizado_em)

data_exame_srt = exame_realizado_em.strftime(STR_FORMATACAO)

print(data_exame_srt)

TEMPO_RESULTADO_EXAME = timedelta(days=2)

print(TEMPO_RESULTADO_EXAME)

previsao_resultado = exame_realizado_em + TEMPO_RESULTADO_EXAME

print(previsao_resultado)

previsao_entrega_str = previsao_resultado.strftime(STR_FORMATACAO)

print(previsao_entrega_str)

print(f'Data de realização do exame: {data_exame_srt}\n\
      Previsão da entrega do resultado: {previsao_entrega_str}')
