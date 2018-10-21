from django.shortcuts import render

# Create your views here.
def index(request):
    #this is your new views
    words = ["my", "please", "that", "and", "what", "a", "there", "i", "we", "are", "is", "were", "was", "you", "they",
             "play", "like", "work", "have", "feel", "read", "more", "stop", "it", "he", "want", "come", "go", "say",
             "color", "help", "she", "dont", "eat", "make", "need", "drink", "turn", "put"]

    # build a list of dictionaries with "word" and "image_url" keys
    word_images = []
    for word in words:
        word_images.append({'word': word,
                            'image_url': '/images/{}.jpg'.format(word)})

    return render(request, 'index.html', {'word_images': word_images})

#TODO populate images dictionary with records from database via Model

#TODO add an upload view and corresponding template

#TODO allow user to choose which icon and voice sets to load
