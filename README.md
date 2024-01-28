# Speed Test Python

This Python script, `speed_test.py`, is designed to measure the performance of different approaches for calculating the sum of integers up to a specified limit. The script utilizes four methods: while loop, for loop, `sum_range`, and `sum_numpy` (c library).

## Usage

To run the speed test using Docker Compose, follow the instructions below.

### Docker Compose Execution

1. Build and run the Docker container:

    ```bash
    docker-compose up --build
    ```

    This command will build the Docker image and run the container based on the configurations in `docker-compose.yml`.

2. View the results:

    The script will print the execution time for each method in the console.

3. Stop and remove the containers:

    ```bash
    docker-compose down
    ```

## Methods

### 1. While Loop

The `while_loop` method uses a while loop to iterate through numbers up to a given limit and calculates their sum.

### 2. For Loop

The `for_loop` method employs a for loop to iterate over a range of numbers and compute their sum.

### 3. Sum Range

The `sum_range` method utilizes the built-in `sum` function with the `range` function to achieve the desired sum.

### 4. Sum Numpy

The `sum_numpy` method leverages the NumPy C library to calculate the sum of an array generated using `numpy.arange`.

## Benchmarking

The script uses the `timeit` module to measure the execution time of each method. The results are printed to the console, allowing for a quick comparison of the performance of different approaches.

## Results

Sample output indicating the execution time for each method will be displayed upon running the script.

## Contributing

Feel free to contribute to this project by opening issues or submitting pull requests. Your feedback and suggestions are highly appreciated.

## License

This project is licensed under the [MIT License](LICENSE), making it open and accessible for collaboration.

---

**Note:** Adjust the script parameters as needed for your specific testing scenarios.
