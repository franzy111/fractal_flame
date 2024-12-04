import logging

from src.generator.fractal_generator import FractalGenerator
from src.ui.command_line_args import CommandLineArgs

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:
    config = CommandLineArgs()
    fractal_generator = FractalGenerator()
    fractal_generator.run(config)


if __name__ == "__main__":
    main()
