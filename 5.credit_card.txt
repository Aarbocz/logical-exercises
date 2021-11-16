# Check is the credit card number is from either Kappa or Gamma and if it's expired

def main():
    credit_cards = [";854922420655947=20087011490683843?", ";722792821249=190220153666234?", ";8657607910110=2209701507597562?", ";6034523459017=24032012187993726?", ";83407977524115=2010701164703842?", ";22554987787910=1903201221224791?", ";7621767951747=21112018460506111?", ";24478927568913=230470179307259?", ";88674481889649=19062014166695784?", ";76985229117350=1805701127970335?", ";2147686439882=2712701977197697?", ";86392841965929=2108201878359745?"]

    # Stores kappa credit cards
    kappa_expired = []

    # Store gamma credit cards
    gamma_expired = []

    # Check if credit card is from kappa or gamma
    for i in range(len(credit_cards)):
        if credit_cards[i][1] == "2":
            if check_expired(credit_cards[i]):
                kappa_expired.append(credit_cards[i])
        elif credit_cards[i][1:3] == "72" or credit_cards[i][1:3] == "76":
            if check_expired(credit_cards[i]):
                gamma_expired.append(credit_cards[i])

    # Print results
    print("Kappa credit card(s) expired: ")
    for card in kappa_expired:
        print(card)

    print()
    print("Gamma credit card(s) expired: ")
    for card in gamma_expired:
        print(card)

# Check if credit card is expired
def check_expired(cc):
    i = cc.find("=")
    year = cc[i+1:i+3]
    month = cc[i+3:i+5]
    if int(year) < 20:
        return True
    elif int(year) == 20 and int(month) >= 11:
        return True
    else:
        return False

main()