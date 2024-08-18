import pandas as pd
import json
from .utilities import *

def build_test_data(book_df):
    return {
        'test_ids': [0, 1, 2],
        'strings': {
            0: '\n"Watch out Rosie!" cried Mum. \n"There\'s a monster behind you." \n"I am going to eat you!" shouted the monster.',
            1: '\nIt was a long drive to the safari park but it was worth it.\nApatosaurus saw an animal just like Triceratops. “That’s a\nrhinoceros,” said Hany.\n“Triceratops has got more horns.”\nMum liked the giraffes best and Nan-\nliked the zebras.\nThe monkeys were funny but the\nman said not to feed them.\nSam asked him if they had pandas but the man said\nno, they were endangered animals.\nHarry wanted to know what endangered meant.\nSam said he was too little to understand.\nNan helped. She bought Harry a book about endangered animals.\nShe thought it was sad about the Sumatran tigers. People kept\nhunting them so there were only a few left in the whole world.\n\nHarry really wanted to help but he had no money. “I\nwant to save some animals,” he said.\n“What can I do, Mum?”\nSam said, “Tuh! What a waste of time!”\nShe said he was miles too small to make any difference.',
            2: book_df.iloc[0].Text
        },
        'task_1_responses': {
            0: {
                'speech_sections': [
                    {
                        'speaker': 'Mum',
                        'recipient': 'Rosie',
                        'speech_text': '\n"Watch out Rosie!" cried Mum. \n"There\'s a monster behind you."',
                        'speech_section_id': 0
                    },
                    {
                        'speaker': 'The monster',
                        'recipient': 'Rosie',
                        'speech_text': '\n"I am going to eat you!" shouted the monster.',
                        'speech_section_id': 1
                    },
                ]

            },
            1: {
                'speech_sections': [
                    {
                        'speaker': 'Hany',
                        'recipient': 'Apatosaurus',
                        'speech_text': '“That’s a\nrhinoceros,” said Hany.\n“Triceratops has got more horns.”',
                        'speech_section_id': 0
                    },
                    {
                        'speaker': 'Harry',
                        'recipient': 'Mum',
                        'speech_text': '“I\nwant to save some animals,” he said.\n“What can I do, Mum?”',
                        'speech_section_id': 1
                    },
                    {
                        'speaker': 'Sam',
                        'recipient': 'Harry',
                        'speech_text': '“Tuh! What a waste of time!”\nShe said he was miles too small to make any difference.',
                        'speech_section_id': 2
                    }
                ]
            },
            2: {
                'speech_sections': [
                    {
                        'speaker': 'St. Nicholas',
                        'recipient': 'Reindeer',
                        'speech_text': 'Now, Dasher! now, Dancer!\nnow, Prancer and Vixen!\nOn Comet! on Cupid!\non Donner and Blitzen!\nTo the top of the porch, to\nthe top of the wall,\nNow, dash away! Dash\naway! Dash away all!',
                        'speech_section_id': 0
                    },
                    {
                        'speaker': 'St. Nicholas',
                        'recipient': 'everyone',
                        'speech_text': 'Happy\nChristmas to all, and to all a good\nnight!',
                        'speech_section_id': 1
                    }
                ]
            }
        },
        'task_2_responses': {
            0: {
                'speech_sections': [
                    {
                        'speaker': 'Mum',
                        'recipient': 'Rosie',
                        'spoken_words_only': 'Watch out Rosie! There\'s a monster behind you.',
                        'speech_section_id': 0
                    },
                    {
                        'speaker': 'The monster',
                        'recipient': 'Rosie',
                        'spoken_words_only': 'I am going to eat you!',
                        'speech_section_id': 1
                    },
                ]

            },
            1: {
                'speech_sections': [
                    {
                        'speaker': 'Hany',
                        'recipient': 'Apatosaurus',
                        'spoken_words_only': 'That’s a rhinoceros. Triceratops has got more horns.',
                        'speech_section_id': 0
                    },
                    {
                        'speaker': 'Harry',
                        'recipient': 'Mum',
                        'spoken_words_only': 'I want to save some animals. What can I do, Mum?',
                        'speech_section_id': 1
                    },
                    {
                        'speaker': 'Sam',
                        'recipient': 'Harry',
                        'spoken_words_only': 'Tuh! What a waste of time!',
                        'speech_section_id': 2
                    }
                ]
            },
            2: {
                'speech_sections': [
                    {
                        'speaker': 'St. Nicholas',
                        'recipient': 'Reindeer',
                        'spoken_words_only': 'Now, Dasher! now, Dancer! now, Prancer and Vixen! On Comet! on Cupid! on Donner and Blitzen! To the top of the porch, to the top of the wall, Now, dash away! Dash away! Dash away all!',
                        'speech_section_id': 0
                    },
                    {
                        'speaker': 'St. Nicholas',
                        'recipient': 'everyone',
                        'spoken_words_only': 'Happy Christmas to all, and to all a good night!',
                        'speech_section_id': 1
                    }
                ]
            }
        },
        'task_3_characters': {
            0: ['Rosie', 'Mum'],
            1: ['Harry', 'Apatosaurus', 'Mum'],
            2: ['Saint Nick', 'Reindeer']
        },
        'task_3_aliases': {
            0: pd.DataFrame({
                'alias': ['Monster'],
                'character': ['Mum']
            }).to_csv(),
            1: pd.DataFrame({
                'alias': ['Sam'],
                'character': ['Mum']
            }).to_csv(),
            2: pd.DataFrame({
                'alias': ['St. Nicholas'],
                'character': ['Saint Nick']
            }).to_csv(),
        },
        'task_3_responses': {
            0: {
                'speech_sections': [
                    {
                        'speaker': 'Mum',
                        'recipient': 'Rosie',
                        'speaker_matched': 'Mum',
                        'recipient_matched': 'Rosie',
    #                     'spoken_words_only': 'Watch out Rosie! There\'s a monster behind you.',
                        'speech_section_id': 0
                    },
                    {
                        'speaker': 'The monster',
                        'recipient': 'Rosie',
                        'speaker_matched': 'Mum',
                        'recipient_matched': 'Rosie',
    #                     'spoken_words_only': 'I am going to eat you!',
                        'speech_section_id': 1
                    },
                ]

            },
            1: {
                'speech_sections': [
                    {
                        'speaker': 'Hany',
                        'recipient': 'Apatosaurus',
                        'speaker_matched': 'Unknown',
                        'recipient_matched': 'Apatosaurus',
    #                     'spoken_words_only': 'That’s a rhinoceros. Triceratops has got more horns.',
                        'speech_section_id': 0
                    },
                    {
                        'speaker': 'Harry',
                        'recipient': 'Mum',
                        'speaker_matched': 'Harry',
                        'recipient_matched': 'Mum',
    #                     'spoken_words_only': 'I want to save some animals. What can I do, Mum?',
                        'speech_section_id': 1
                    },
                    {
                        'speaker': 'Sam',
                        'recipient': 'Harry',
                        'speaker_matched': 'Mum',
                        'recipient_matched': 'Harry',
    #                     'spoken_words_only': 'Tuh! What a waste of time!',
                        'speech_section_id': 2
                    }
                ]
            },
            2: {
                'speech_sections': [
                    {
                        'speaker': 'St. Nicholas',
                        'recipient': 'Reindeer',
                        'speaker_matched': 'Saint Nick',
                        'recipient_matched': 'Reindeer',
    #                     'spoken_words_only': 'Now, Dasher! now, Dancer! now, Prancer and Vixen! On Comet! on Cupid! on Donner and Blitzen! To the top of the porch, to the top of the wall, Now, dash away! Dash away! Dash away all!',
                        'speech_section_id': 0
                    },
                    {
                        'speaker': 'St. Nicholas',
                        'recipient': 'everyone',
                        'speaker_matched': 'Saint Nick',
                        'recipient_matched': 'The Reader',
    #                     'spoken_words_only': 'Happy Christmas to all, and to all a good night!',
                        'speech_section_id': 1
                    }
                ]
            }
        }
    }


def run_task_1_test_i(test_id, test_data, completion, verbose=False):
    response = json.loads(completion.choices[0].message.content)
    correct_speech_sections = test_data['task_1_responses'][test_id]['speech_sections']

    try:
        assert len(response['speech_sections']) == len(correct_speech_sections)
    except AssertionError:
        print(f"Failed test: speech section lists are different lengths.")
        if verbose:
            print(response['speech_sections'])
            print(correct_speech_sections)

    test_elemtents = {
        'speaker': {
            'case_sensitive': False,
            'remove_leading_the': True
        },
        'recipient': {
            'case_sensitive': False,
            'remove_leading_the': True
        },
        'speech_text': {
            'case_sensitive': True,
            'remove_leading_the': False
        },
    }

    for correct_section, section in zip(correct_speech_sections, response['speech_sections']):
        pass_flag = True

        try:
            assert section['speech_section_id'] == correct_section['speech_section_id']
        except AssertionError:
            print(f"Failed test: speech section_id not equal.")
            if verbose:
                print(correct_section)
                print(section)

        for element in test_elemtents.keys():
            try:
                assert compare_strings(
                    correct_section[element],
                    section[element],
                    _case_sensitive=test_elemtents[element]['case_sensitive'],
                    _remove_leading_the=test_elemtents[element]['remove_leading_the']
                )
            except AssertionError:
                print(f"Failed {element} test for section: {section}")
                if verbose:
                    print(correct_section[element])
                pass_flag = False

    return pass_flag