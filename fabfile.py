# -*- coding: utf-8 -*-
"""fabric 部署脚本"""

import os
import datetime
from fabric.api import *

go_path = os.environ.get("GOPATH", None)
if go_path is None:
    raise Exception("GOPATH unset!")
def build():
    command = "GOOS=linux go build"
    # command = "git archive --format tar.gz -o dist/%s master" % project_tar_name
    local(command, capture=False)
