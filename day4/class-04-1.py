start_num = 0
for i in range(10):
    start_num += 1
    print(start_num)

word_count = {}
sample_words = "this is a sample sentence with many words this is a sample"
for word in sample_words.split():
    if word not in word_count:
        word_count[word] = 1
    else:
        word_count[word] += 1
