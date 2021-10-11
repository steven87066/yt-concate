from yt_concate.pipeline.steps.get_videos_list import GetVideosList
from yt_concate.pipeline.steps.steps import StepException
from yt_concate.pipeline.pipeline import PipeLine

CHANNEL_ID = 'UCwn0jaGbgMkYioOWBzMog1Q'


def main() :
    inputs = {
        'channel_id': CHANNEL_ID
    }
    steps = [
        GetVideosList(),
              ]

    p= PipeLine(steps)
    p.run(inputs)


if __name__ == '__main__':
    main()
