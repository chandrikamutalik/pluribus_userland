#!/usr/bin/python
#
# CDDL HEADER START
#
# The contents of this file are subject to the terms of the
# Common Development and Distribution License (the "License").
# You may not use this file except in compliance with the License.
#
# You can obtain a copy of the license at usr/src/OPENSOLARIS.LICENSE
# or http://www.opensolaris.org/os/licensing.
# See the License for the specific language governing permissions
# and limitations under the License.
#
# When distributing Covered Code, include this CDDL HEADER in each
# file and include the License file at usr/src/OPENSOLARIS.LICENSE.
# If applicable, add the following below this CDDL HEADER, with the
# fields enclosed by brackets "[]" replaced with your own identifying
# information: Portions Copyright [yyyy] [name of copyright owner]
#
# CDDL HEADER END
#

# Copyright 2009 Sun Microsystems, Inc.  All rights reserved.
# Use is subject to license terms.

from pkg.misc import Singleton

class DebugValues(dict):
        """Singleton dict that returns None if unknown value
        is referenced"""
        __metaclass__ = Singleton

        def __getitem__(self, item):
                """ returns None if not set """
                return self.get(item, None)

        def get_value(self, key):
                return self[key]

        def set_value(self, key, value):
                self[key] = value

DebugValues=DebugValues()
