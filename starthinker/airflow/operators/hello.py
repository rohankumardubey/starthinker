###########################################################################
#
#  Copyright 2020 Google LLC
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
###########################################################################

import time

from airflow import models
from airflow.utils.decorators import apply_defaults


class Hello(models.BaseOperator):

  @apply_defaults
  def __init__(self, say='', sleep=0, **kwargs):
    self.say = say
    self.sleep = sleep
    super(Hello, self).__init__(**kwargs)

  def execute(self, context):
    print(self.say)
    if self.sleep:
      time.sleep(self.sleep)
