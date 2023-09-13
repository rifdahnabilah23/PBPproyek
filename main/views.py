from django.shortcuts import render

# Create your views here.

# def show_main(request):
#     context = {
#         'name': 'Pak Bepe',
#         'class': 'PBP A'
#     }

#     return render(request, "main.html", context)


def show_main(request):
    context = {
        'nama' : 'Rifdah Nabilah',
        'kelas' : 'PBP B',
        'buah1': 'Melon', 
        'buah2': 'Strawberry',
        'buah3': 'Alpukat',
        'stok1': 20, 
        'stok2': 15,
        'stok3': 25,
        'harga1': 20000, 
        'harga2': 12000,
        'harga3': 10000,
        'keterangan1': 'Buah Melon yang kaya akan nutrisi mengandung kalium, asam folat, protein, vitamin C, dan magnesium.',
        'keterangan2': 'Buah Strawberry yang kaya akan antioksidan, vitamin C, kalium, vitamin B9(asam folat), dan mangan.',
        'keterangan3': 'Buah Alpukat mengandung  nutrisi, vitamin B, vitamin K, kalium, tembaga, vitamin E, dan vitamin C.',
    }

    return render(request, "main.html", context)
