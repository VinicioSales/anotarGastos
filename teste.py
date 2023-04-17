import re

texto = """Deu tudo certo com a sua transferência 

|

|  |  |  ![](https://staging-
cdn.nubank.com.br/engagement_machine/photos/logo.png)  
---  
  
|  
  
---  
  
|  |  
  
---  
  
Transferência realizada para sua outra conta

|  |

---

Olá, Vinício


A transferência para **sua conta no QI Sociedade de Credito Direto S.A.** foi
realizada com sucesso.

|  |

Valor Enviado

---

**R$ 1,00**

17 ABR às 12:01

---

|

|  |

**Abraços,
Equipe Nubank
**

---

Por favor, pedimos que você não responda esse e-mail, pois se trata de uma
mensagem automática e não é possível dar continuidade com seu atendimento por
aqui.

|  |  |  |  [ ![](https://s3.amazonaws.com/ss-
usa/companies/MzawMDExMzS2AAA/uploads/Nubank/facebook_60.png)
](http://www.facebook.com/nubank)
---
|  [ ![](https://s3.amazonaws.com/ss-
usa/companies/MzawMDExMzS2AAA/uploads/Nubank/twitter_60.png)
](https://twitter.com/nubank)
---
|  [ ![](https://s3.amazonaws.com/ss-
usa/companies/MzawMDExMzS2AAA/uploads/Nubank/instagram_60.png)
](http://www.instagram.com/nubank)
---
|  [ ![](https://s3.amazonaws.com/ss-
usa/companies/MzawMDExMzS2AAA/uploads/Nubank/youtube_60.png)
](https://www.youtube.com/channel/UCgsDX3hTwiPdtGHJjMFfDxg)
---

|  |

Caso ainda tenha dúvidas, acesse **[ Me Ajuda
](https://nuapp.nubank.com.br/bnVhcHA6Ly9udWhlbHA/dXRtX3NvdXJjZT1lbWFpbA==) **
diretamente no seu aplicativo.

Para emergências ligue para 0800 591 2117. Atendimentos são realizados 24
horas, todos os dias pelo chat ou telefone.

---

Não deseja receber mais nossos nossos emails? [ clique aqui para se
descadastrar. ](https://webapp-proxy-
webhooks.nubank.com.br/api/webhooks/email-
unsubscribe/AP5QVO5mCR4xeW4ZBa4MbR7sNjopAn-7hXmTs6qKmOD0wQPTGE41arCbvqlZF9dSNwWng3HS5se2mTAmiP_wf4ebWiaCFwAX4wTXflLXcAek5jAMfRwiPzQr8vKRHj2_qEVd5vkKir9AQv9amKAJLskSWyn15f6pXUHROg6jlbJzvN9lMLX1szC3NUWUXXpgrCl_QBHXXe90b9KU3cRXMxb-518X0K2IZZ95O2dGBZzMbdDkotDXVoHo-
IXIdx4lEXcEJsM-
GHOSQzRGyBsdVH512yNDtoSOtg.ADBfDS5b-1vIW1Agw_erYz7_2ECdVl75YGpXHd3lN_X9Cn9NnoMPgeaaKtII6azv7FOmKiARw2zHk4kwu5kE0tjzwWVA3uax90R8cBaYJjMGnJzUetZT-
im7GJo__H7R3j9HYHv0kPbOoRGg5L8pJOS-c0uPYXliqF1PK-t_1ng9Ttk2Ig) .

|  |

Nu Pagamentos S.A - Instituição de Pagamento 18.236.120/0001-58
Rua Capote Valente, 39 - 05409-000- São Paulo - SP

---

![](http://email.nubank.com.br/o/eJwcz72upDAMhuGrgc7Izj9F2rkPJ3HORgsBQWY0e_crTmn5fYqvxFxE8iyRXCBvtHM0_4kZLRJqVijouBA7rN6XQsJS67rOLSpUGg15ekpavLcBa2BLHgtlNRns78T975KPfUnX3N-Qjz44D2gl2ioYaF1Bh6DAuCyQjEtAVdnVGvHGpofId8jVeXvMWqxOmBVYDhq0rh6CcwgmE6dqUvHq15zXMY7x75R4
--cesp8bD4HOu8SbP63_3JN6jYv7XeWC4z3glj4m9ZKd2_Y8b9kqnO07qddHzVf8tN5yO5ab-
xjceTL487TPvP8BAAD__841ZIk)"""

#padrao = r'A transferência para \*\*(.*)\*\* foi realizada com sucesso\.'
padrao = r"(?<=\*\*)(.*?)(?=\*\*)"
match = re.search(padrao, texto)
if match:
    store = match.group(1)
    print(store)
