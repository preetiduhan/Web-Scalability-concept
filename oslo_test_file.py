import sys
from oslo_config import cfg
grp=cfg.OptGroup('mygroup')
opts=[cfg.StrOpt('name'),cfg.IntOpt('age',default=23)]
cfg.CONF.register_group(grp)
cfg.CONF.register_opts(opts,group=grp)
cfg.CONF(sys.argv[1:])
print("The value of option1 is %s" % cfg.CONF.mygroup.name)
print("The value of option2 is %d" % cfg.CONF.mygroup.age)
