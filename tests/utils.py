class ResponsesGen:
    def __init__(self, responses):
        self.responses = responses
        self.cur_index = -1
        self.input_messages = []

    def __call__(self, input_message=''):
        self.input_messages.append(input_message)
        if self.responses == '':
            return ''
        else:
            self.cur_index += 1
            return self.responses[self.cur_index]

