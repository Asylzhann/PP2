def pal(s):
    return s==s[::-1]
print(pal(input("phrase: ")))