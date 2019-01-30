"""
Copyright (C) 2017-2018 Zijad Kurtanovic <kurtanovic@informatik.uni-hamburg.de>

This file is part of URMiner and subject to the terms and conditions defined in
file 'LICENSE.txt', which is part of this source code package.
"""


from flask import Blueprint, jsonify

from flask_restful import Resource
from flask_restful_swagger_2 import Api
from URMiner.classifier_ur.data import COL_HAS_ALTERNATIVE
from URMiner.services_ur import (RESPONSE_DATA_KEY, RESPONSE_ERROR_KEY,
                                 _get_review_clf, _get_sentence_clf,
                                 review_request_parser,
                                 sentence_request_parser)

URI_REVIEW_ALTERNATIVE_CLF = "/hitec/urminer-review/alternative"      # % URI_ROOT_REVIEW_MINER
URI_SENTENCE_ALTERNATIVE_CLF = "/hitec/urminer-sentence/alternative"    # % URI_ROOT_SENTENCE_MINER

_bp = Blueprint("alternative", __name__)
_api = Api(_bp)#api_spec_url='/api/%s/swagger' % _bp.name)

def get_blueprint():
    return _bp

def add_to_api(api):
    api.add_resource(AlternativeReviewClf, URI_REVIEW_ALTERNATIVE_CLF)
    api.add_resource(AlternativeSentenceClf, URI_SENTENCE_ALTERNATIVE_CLF)

class AlternativeReviewClf(Resource):
    ALTERNATIVE_REVIEW_CLF = _get_review_clf(COL_HAS_ALTERNATIVE, "baseline")

    def post(self):
        # logging.debug("received title: %s" % title)
        req_data = review_request_parser.parse_args()
        print(req_data)
        try:
            result = self.ALTERNATIVE_REVIEW_CLF.predict_dict(req_data)
            result = jsonify({RESPONSE_DATA_KEY : result})
            return result

        except Exception as e:
            r = jsonify({RESPONSE_ERROR_KEY: str(e)})
            r.status_code = 500

        return r

class AlternativeSentenceClf(Resource):
    ALTERNATIVE_SENTENCE_CLF = _get_sentence_clf(COL_HAS_ALTERNATIVE, "baseline_sentence")

    def post(self):
        # logging.debug("received title: %s" % title)
        req_data = sentence_request_parser.parse_args()
        print(req_data)
        try:
            result = self.ALTERNATIVE_SENTENCE_CLF.predict_dict(req_data)
            result = jsonify({RESPONSE_DATA_KEY: result})
            return result

        except Exception as e:
            r = jsonify({RESPONSE_ERROR_KEY: str(e)})
            r.status_code = 500

        return r
