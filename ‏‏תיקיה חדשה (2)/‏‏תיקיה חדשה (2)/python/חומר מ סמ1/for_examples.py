for i in range(1, 100):  # for(int i=1;i<100;i++)
    print(i)

for i in range(100):  # for(int i=0;i<100;i++)
    print(i)

for i in range(1, 100, 2):  # for(int i=1;i<100;i+=2)
    print(i)

"""
for(int i=1;i<100;i++)
{
    for(int j=1;j<100;j++)
    {
        //Display something
    }
}
"""
for i in range(1, 10):
    for j in range(1, 5):
        print(i, j)
