article = "In Syria, Trump Distills a Foreign Policy of Impulse, and Faces the Fallout By Peter Baker and Lara Jakes Oct. 10, 2019 WASHINGTON — No one should have been surprised, and yet it seems that everyone was. President Trump made clear long ago that he wanted to get out of the Middle East, but even some of his own supporters evidently assumed that he would not follow through or that someone would stop him. As a result, the international crisis that many of his opponents feared for so long has finally arrived, but it is one of Mr. Trump’s own making and one that pits him against his own party and his own government. The Turkish assault on America’s Kurdish allies that he effectively facilitated reflects his foreign policy in its rawest Trumpian form. It is a foreign policy built primarily on reflex and increasingly resistant to outside advice. Unimpressed by the national security establishment and uninterested in the tedium of traditional policymaking, Mr. Trump often demonstrates more faith in what some overseas strongman tells him than the soft-boiled guidance of the bureaucrats, diplomats, intelligence analysts and military officers in the Situation Room. “This may be the riskiest national security decision that he’s made to this point,” said Richard Fontaine, the chief executive of the Center for a New American Security and a former aide to President George W. Bush. “I don’t know that we’ve learned anything new about the president’s decision-making style, but it does reveal the very significant risks that that style carries.” Having upended Middle East policy with the flick of a Twitter finger, however, Mr. Trump now is trying to find a way to reverse the eminently foreseeable consequences as Turkish forces bombard the same Kurdish fighters who helped the United States overpower the Islamic State. Defense Secretary Mark T. Esper called his Turkish counterpart on Thursday to stress that Washington opposes the incursion into Syria, and Mr. Trump talked of brokering some form of peace between Turkey and the Kurds. “I hope we can mediate,” he told reporters even as he contemplates sanctions against Turkey. But the administration signaled that it was still giving the Turks a degree of latitude. A State Department official, who briefed reporters under ground rules that he not be identified, said the administration would impose costs if Turkey went “beyond the lines,” which he defined as ethnic cleansing or indiscriminate artillery and airstrikes directed at civilians. That would suggest that Turkish forces that crossed the border into northern Syria on Wednesday could hit Kurdish fighters hard, but not slaughter them, without provoking American reaction. At the same time, the Kurds have been counterattacking, firing off shells at Turkish border villages as the danger of escalation spiraled."
article = article.lower()

d = {}

for s in article:
    if s in d.keys():
        d[s] += 1
    else:
        d[s] = 1


chars_top10 = sorted((value, key) for (key, value) in d.items())[-10:]
chars_top10.reverse()

###################

for p in "“”’.—,-":
    article = article.replace(p, "")

words = article.split(" ")

d = {}

for w in words:
    if w in d.keys():
        d[w] += 1
    else:
        d[w] = 1

words_top30 = sorted((value, key) for (key, value) in d.items())[-30:]
words_top30.reverse()

############ fibonacci sequence with a memory


def fib_dict(n, d={1: 1, 2: 1}):
    if n in d:
        return d[n]
    else:
        fib_n = fib_dict(n - 1, d) + fib_dict(n - 2, d)
        d[n] = fib_n
        return fib_n


fib_dict(6)
fib_dict(35)
fib_dict(100)

######################################

# f(n)=f(n-1)+f(n-2)


def fibo(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return fibo(n - 1) + fibo(n - 2)


def Fibbonac(K):
    i = 1
    l = []
    while i <= K:
        l += [fibo(i)]
        i += 1
    return l


print(Fibbonac(6))
print(Fibbonac(10))
print(Fibbonac(15))

x = "dsgfkldsf"
x[::-1]
