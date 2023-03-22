from primeqa.components.reader.extractive import ExtractiveReader

reader = ExtractiveReader(model="PrimeQA/nq_tydi_sq1-reader-xlmr_large-20221110")
reader.load()


class RCPrediction:
    def answer(self, question, context):
        answers = reader.predict([question], [[context]])
        return answers["0"][0]["span_answer_text"]
