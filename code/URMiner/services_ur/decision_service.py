"""
Copyright (C) 2017-2018 Zijad Kurtanovic <kurtanovic@informatik.uni-hamburg.de>

This file is part of URMiner and subject to the terms and conditions defined in
file 'LICENSE.txt', which is part of this source code package.
"""


from flask import jsonify

from flask_restful import Resource
from URMiner.classifier_ur.data import (COL_HAS_ACQUIRE_DECISION,
                                        COL_HAS_DECISION)
from URMiner.services_ur import (RESPONSE_DATA_KEY, RESPONSE_ERROR_KEY,
                                 _get_review_clf, _get_sentence_clf,
                                 review_request_parser,
                                 sentence_request_parser)

URI_REVIEW_DECISION_CLF = "/hitec/urminer-review/decision" #"/%s/decision" % URI_ROOT_REVIEW_MINER
URI_SENTENCE_DECISION_CLF = "/hitec/urminer-sentence/decision" #"/%s/decision" % URI_ROOT_SENTENCE_MINER

URI_REVIEW_ACQUIRE_CLF = "/hitec/urminer-review/decision/acquire" #"/%s/decision" % URI_ROOT_REVIEW_MINER
URI_SENTENCE_ACQUIRE_CLF = "/hitec/urminer-sentence/decision/acquire" #"/%s/decision" % URI_ROOT_SENTENCE_MINER

# _bp = Blueprint("decision", __name__)
#api_spec_url='/api/%s/swagger' % _bp.name)

def get_blueprint():
    return _bp

def add_to_api(api):
    # _api = Api(_bp)
    api.add_resource(DecisionReviewClf, URI_REVIEW_DECISION_CLF)
    api.add_resource(DecisionSentenceClf, URI_SENTENCE_DECISION_CLF)

    api.add_resource(AcquireDecisionReviewClf, URI_REVIEW_ACQUIRE_CLF)
    api.add_resource(AcquireDecisionSentenceClf, URI_SENTENCE_ACQUIRE_CLF)
#
# Middle Layer endpoints
#

class DecisionReviewClf(Resource):
    DECISION_REVIEW_CLF = _get_review_clf(COL_HAS_DECISION, "baseline")

    def post(self):
        # logging.debug("received title: %s" % title)
        req_data = review_request_parser.parse_args()

        try:
            result = self.DECISION_REVIEW_CLF.predict_dict(req_data)
            result = jsonify({RESPONSE_DATA_KEY : result})
            return result

        except Exception as e:
            r = jsonify({RESPONSE_ERROR_KEY: str(e)})
            r.status_code = 500

        return r

class DecisionSentenceClf(Resource):
    DECISION_SENTENCE_CLF = _get_sentence_clf(COL_HAS_DECISION, "baseline_sentence")

    def post(self):
        # logging.debug("received title: %s" % title)
        req_data = sentence_request_parser.parse_args()

        try:
            result = self.DECISION_SENTENCE_CLF.predict_dict(req_data)
            result = jsonify({RESPONSE_DATA_KEY: result})
            return result

        except Exception as e:
            r = jsonify({RESPONSE_ERROR_KEY: str(e)})
            r.status_code = 500

        return r

#
# Basic Layer endpoints
#
class AcquireDecisionReviewClf(Resource):
    ACQUIRE_REVIEW_CLF = _get_review_clf(COL_HAS_ACQUIRE_DECISION, "baseline")

    def post(self):
        # logging.debug("received title: %s" % title)
        req_data = review_request_parser.parse_args()

        try:
            result = self.ACQUIRE_REVIEW_CLF.predict_dict(req_data)
            result = jsonify({RESPONSE_DATA_KEY: result})
            return result

        except Exception as e:
            r = jsonify({RESPONSE_ERROR_KEY: str(e)})
            r.status_code = 500

        return r

class AcquireDecisionSentenceClf(Resource):
    ACQUIRE_SENTENCE_CLF = _get_sentence_clf(COL_HAS_ACQUIRE_DECISION, "baseline_sentence")

    def post(self):
        # logging.debug("received title: %s" % title)
        req_data = sentence_request_parser.parse_args()

        try:
            result = self.ACQUIRE_SENTENCE_CLF.predict_dict(req_data)
            result = jsonify({RESPONSE_DATA_KEY: result})
            return result

        except Exception as e:
            r = jsonify({RESPONSE_ERROR_KEY: str(e)})
            r.status_code = 500

        return r
