# -*- coding: utf-8 -*-
from decorated.function import Function, BoundedFunction, PartialFunction
from decorated.util.conditional import Conditional
from decorated.util.remove_extra_args import RemoveExtraArgs
from decorated.util.retries import Retries

Function = Function
PartialFunction = PartialFunction
BoundedFunction = BoundedFunction

retries = Retries
conditional = Conditional
remove_extra_args = RemoveExtraArgs
