import os

import sys

# UR_GRANULARITY_SENTENCE = "sentence"
# UR_GRANULARITY_REVIEW = "review"
from URMiner.consts_ur import ROOT_DIR

UR_REVIEW_CSV_FILE = "%s/%s" % (ROOT_DIR, "data_repository/labeled_data/comment_data.csv")
UR_SENTENCE_CSV_FILE = "%s/%s" % (ROOT_DIR, "data_repository/labeled_data/sentence_data.csv")

COL_BODY_TYPE = "BodyType"

COL_HAS_ISSUE="HasIssue"
COL_HAS_ALTERNATIVE="HasAlternative"
COL_HAS_ALTERNATIVE_="HasAlternative_"
COL_HAS_ALTFEATURE="HasAltFeature"
COL_HAS_ALTVERSION="HasAltVersion"
COL_HAS_ALTSOFTWARE="HasAltSoftware"


COL_HAS_CRITERIA="HasCriteria"
COL_HAS_CRITERIA_="HasCriteria_"
COL_HAS_USABILITY = "HasUsability"
COL_HAS_RELIABILITY = "HasReliability"
COL_HAS_PERFORMANCE = "HasPerformance"
COL_HAS_SUPPORTABILITY = "HasSupportability"

COL_HAS_JUSTIFICATION= "HasJustification"

COL_HAS_DECISION="HasDecision"
COL_HAS_DECISION_="HasDecision_"
COL_HAS_ACQUIRE_DECISION = "HasAcquire"
COL_HAS_UPDATE_DECISION = "HasUpdate"
COL_HAS_SWITCH_DECISION = "HasSwitch"
COL_HAS_RELINQUISH_DECISION = "HasRelinquish"

UR_MAIN_LABEL_COLUMNS = [COL_HAS_ISSUE, COL_HAS_ALTERNATIVE, COL_HAS_CRITERIA, COL_HAS_DECISION, COL_HAS_JUSTIFICATION]
UR_MAIN_LABEL_CAPTIONS = ["Issue", "Alternative", "Criteria", "Decision", "Justification"]
UR_LABEL_COLUMNS_SUBCONCEPTS = [COL_HAS_ISSUE,
                                COL_HAS_ALTFEATURE, COL_HAS_ALTVERSION, COL_HAS_ALTSOFTWARE,
                                COL_HAS_USABILITY, COL_HAS_RELIABILITY, COL_HAS_PERFORMANCE, COL_HAS_SUPPORTABILITY,
                                COL_HAS_ACQUIRE_DECISION, COL_HAS_UPDATE_DECISION, COL_HAS_SWITCH_DECISION, COL_HAS_RELINQUISH_DECISION,
                                COL_HAS_JUSTIFICATION]
UR_LABEL_ALTERNATIVE_SUBCONCEPTS = [COL_HAS_ALTFEATURE, COL_HAS_ALTVERSION, COL_HAS_ALTSOFTWARE]
UR_LABEL_CRITERIA_SUBCONCEPTS = [COL_HAS_USABILITY, COL_HAS_RELIABILITY, COL_HAS_PERFORMANCE, COL_HAS_SUPPORTABILITY]
UR_LABEL_DECISION_SUBCONCEPTS = [COL_HAS_ACQUIRE_DECISION, COL_HAS_UPDATE_DECISION, COL_HAS_SWITCH_DECISION, COL_HAS_RELINQUISH_DECISION]

UR_LABEL_CAPTIONS_SUBCONCEPTS = ["Issue",
                              "Alt. Feat.", "Alt. Version", "Alt. Software",
                              "Usability", "Reliability", "Performance", "Supportability",
                              "Acquire", "Update", "Switch", "Relinquish",
                              "Justification"]

COL_TEXT_BODY = "Body"
COL_TEXT_TITLE = "Title"
COL_RATING="Rating"
COL_INDEX_SENTENCE="RelativeOrder"

COL_CUSTOM_REVIEW_ID = "CustomReviewId"