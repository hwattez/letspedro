
for i in range(0, 51):
    v = 1 if i%2==0 or i < 25 else 1.2

    print(f'''
{i*2}% {{
    transform: scale({v});
}}
    ''')