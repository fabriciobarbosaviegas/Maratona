emails = []
for i in range(int(input())):
    emails.append(input().split('@'))

for i in range(len(emails)):
    emails[i][0] = emails[i][0].replace('.','')

    plusPosition = emails[i][0].find('+')
    if plusPosition >= 0:
        emails[i] = emails[i][0][:plusPosition]
    emails[i] = '@'.join(emails[i])
emails = [*set(emails)]

print(len(emails))