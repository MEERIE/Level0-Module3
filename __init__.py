
def openVault(maxCombo):

    passcode = random.randint(0, 10000)

    for combo in range(maxCombo):

        if combo == passcode:

            return true

    return false
openVault(0)
