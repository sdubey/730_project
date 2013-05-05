def runJob(MRJobClass, input_file, output_dir):
    argsArr = [input_file, '--output-dir=%s' %(output_dir)]
    print "starting %s job " % (MRJobClass.__name__)
    mrJob = MRJobClass(args=argsArr)
    runner = mrJob.make_runner()
    runner.run()
    print "finished %s job" % MRJobClass.__name__
    return mrJob, runner