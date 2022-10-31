from mrjob.job import MRJob

class MRCountingJob(MRJob):

    def mapper(self, _, value):
        self.increment_counter('group', 'lines', 1)
        yield _, value

if __name__ == '__name__':
    MRCountingJob.run()