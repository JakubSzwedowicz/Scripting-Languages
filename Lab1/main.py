# Author: Jakub Szwedowicz
# Date: 10.03.2022
# e-mail: kuba.szwedowicz@gmail.com

def task_1():
    print('Hello!')

    n_files = 3
    # files = [input('Add filename with its extension: ') for _ in range(0, n_files)]
    files = ['a.txt', 'b.txt', 'c.pdf']
    files.sort()

    files_per_extension = dict()
    for file in files:
        file_ext = file.rsplit('.', 1)
        if file_ext[1] not in files_per_extension:
            files_per_extension[file_ext[1]] = [file]
        else:
            files_per_extension[file_ext[1]].append(file)

    f = lambda v: len(v)
    ext_count = {k: f(v) for k, v in files_per_extension.items()}
    print(ext_count)


def task_2():
    text_1 = '#love #tumblr #memes #quotes #funnytexts #texting #funny #tweets #textpost #texture #frasi #tweegram ' \
             '#tweet #tweetext #tweetexts #texgram #tweedride #instapage #tweembler #frasier #frasitumblr #tweeter ' \
             '#tweemblers #tweeters #frasista #textmessage #frasistas #bhfyp'

    text_1_replace = text_1.replace('#', '')
    text_1_replace_split = text_1_replace.split(' ')
    print(text_1_replace_split)

    f = lambda v: len(v)
    letters_per_word = {word: f(word) for word in text_1_replace_split}
    print('Letters per word in text 1 are: \n', letters_per_word)


    text_2 = 'A hashtag is a metadata tag that is prefaced by the pound sign or hash symbol, # (not to be confused ' \
             'with the pound currency sign). Hashtags are used on microblogging and photo-sharing services such as ' \
             'Twitter, Instagram and WeChat as a form of user-generated tagging that enables cross-referencing of ' \
             'content; that is, sharing a topic or theme. For example, a search within Instagram for the hashtag ' \
             '#bluesky returns all posts that have been tagged with that hashtag. After the initial hash symbol, ' \
             'a hashtag may include letters, digits, and underscores. ' \
             'The use of hashtags was first proposed by American blogger, product consultant and speaker Chris' \
             ' Messina in a 2007 tweet. Messina made no attempt to patent the use because he felt "they were born ' \
             'of the internet, and owned by no one". In 2013, Twitter purportedly told the Wall Street Journal that ' \
             '"these things are for nerds" and their use "wouldn\'t be adopted widely". By the end of the decade, ' \
             'though, hashtags were entrenched in the culture of the platform, and they soon emerged across Instagram,' \
             ' Facebook, and YouTube. In June 2014, hashtag was added to the Oxford English Dictionary, as "a word or' \
             ' phrase with the symbol # in front of it, used on social media websites and apps so that you can search' \
             ' for all messages with the same subject".'

    text_2_replace = text_2.replace(',', ';')
    in_count = text_2_replace.lower().count(' in ')
    print('There are {0} words "in"'.format(in_count))

    unique_words = [set(text_1), set(text_2)]
    print('Unique set of characters for \ntext 1 = {0}\n text 2 = {1}'.format(unique_words[0], unique_words[1]))


    text_2_split = text_2.split('.')
    text_2_split[0] = text_2_split[0].capitalize()
    text_2_split[1] = text_2_split[1].upper()
    text_2_split[2] = text_2_split[2].lower()
    text_2_split[3] = ' '.join(elem.capitalize() for elem in text_2_split[3].split())
    text_2_split[4] = text_2_split[4].swapcase()

    for i in range(0, 5):
        print('Line {0} = {1}'.format(i, text_2_split[i]))
    # print(text_2_split)


def main():
    task_1()
    task_2()


if __name__ == '__main__':
    main()
