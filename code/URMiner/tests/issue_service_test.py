"""
Copyright (C) 2017-2018 Zijad Kurtanovic <kurtanovic@informatik.uni-hamburg.de>

This file is part of URMiner and subject to the terms and conditions defined in
file 'LICENSE.txt', which is part of this source code package.
"""

import logging

from classifier_ur.data import COL_TEXT_BODY, COL_TEXT_TITLE, COL_RATING

logging.basicConfig(level=logging.DEBUG)

from flask import Flask, json
import unittest

from services_ur import issue_service

class IssueServiceTestCase(unittest.TestCase):

    def setUp(self):

        self.app = Flask(__name__)
        self.app.testing = True

        # register blueprint
        bp = issue_service.get_blueprint()
        self.app.register_blueprint(bp)

        self.client = self.app.test_client
        self.review_param = {
                COL_TEXT_TITLE :   "Heavy Navy",
                COL_TEXT_BODY:     "I bought this product because I am a long time committed Quicken user, "
                             "and I was not willing to switch to the Mac version when I bought a iMac computer, "
                             "based on the terrible reviews of the software.Parallels has made it possible for me "
                             "to run Quicken 2014 easily.My only complaint is that my son likes to play video games "
                             "and I tried to use parallels with Steam and their game Space Engineers, but the video "
                             "adapter used by Parallels isn't compatible.",
               COL_RATING : 3}

        self.sentence_param = {"body": "This is a shorter text.",
                               "rating": 5}


        # set content type
        # for param in [self.review_param, self.sentence_param]:
        #     param.update({"Content-Type" : "application/json"})

                # binds the urminer_app to the current context
                # with self.urminer_app.app_context():
                #     # create all tables
                #     db.create_all()

        #
        # test data

    def test_review_clf(self):
        res = self.client().post(issue_service.URI_REVIEW_ISSUE_CLF,
                                 data=json.dumps(self.review_param),
                                 content_type='application/json')

        self.assertEqual(res.status_code, 200)

        # test removal of stopwords
        # response = test_client.post(issue_service.URI_REVIEW_CLF, data=review_param)
        # response_json = loads(response.data)
        #
        # # assert response_json["text_preprocessed"] == "bought product long time committed quicken user , willing switch mac " \
        # #                                              "version bought imac computer , " \
        # #                                              "based terrible reviews software.parallels possible run quicken 2014 easily.my " \
        # #                                              "complaint son likes play video games tried use parallels steam game space engineers , " \
        # #                                              "video adapter used parallels n't compatible ."
        # print(response_json)
        #
        # # test removal of stopwords
        # response = test_client.post(preprocessor_bp.URI_REMOVESTOPS,
        #                                         data=data_param2)
        # response_json = loads(response.data)
        # assert response_json["text_preprocessed"] == 'shorter text .'
        # print(response_json)

    def test_sentence_clf(self):
        res = self.client().post(issue_service.URI_SENTENCE_ISSUE_CLF,
                                 data=json.dumps(self.review_param),
                                 content_type='application/json')

        self.assertEqual(res.status_code, 200)

if __name__ == "__main__":
    # logging.basicConfig(level=logging.DEBUG)
    unittest.main()
    # tst =IssueServiceTestCase()
    # tst.setUp()
    # tst.test_review_clf()