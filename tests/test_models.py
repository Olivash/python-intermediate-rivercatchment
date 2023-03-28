"""Tests for statistics functions within the Model layer."""

import pandas as pd
import pandas.testing as pdt
import datetime
import pytest

@pytest.mark.parametrize(

    "test_data,test_index,test_columns,expected_data,expected_index,expected_columns",
    [

        (
                [[0.0, 0.0], [0.0, 0.0], [0.0, 0.0]],
                [pd.to_datetime('2000-01-01 01:00'),
                 pd.to_datetime('2000-01-01 02:00'),
                 pd.to_datetime('2000-01-01 03:00')],
                ['A', 'B'],
                [[0.0, 0.0]],
                [datetime.date(2000, 1, 1)],
                ['A', 'B']

        ),
        (
                [[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]],
                [pd.to_datetime('2000-01-01 01:00'),
                 pd.to_datetime('2000-01-01 02:00'),
                 pd.to_datetime('2000-01-01 03:00')],
                ['A', 'B'],
                [[3.0, 4.0]],
                [datetime.date(2000, 1, 1)],
                ['A', 'B']

        )

    ]
)
def test_daily_mean(test_data,test_index,test_columns,expected_data,expected_index,expected_columns):
    """Test mean functions works with zeros and postive integers"""
    from catchment.models import daily_mean
    pdt.assert_frame_equal(daily_mean(pd.DataFrame(data=test_data,index=test_index,columns=test_columns)),
                           pd.DataFrame(data=expected_data,index=expected_index,columns=expected_columns)

                    )




def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""
    from catchment.models import daily_mean

    test_input = pd.DataFrame(
                     data=[[0.0, 0.0],
                           [0.0, 0.0],
                           [0.0, 0.0]],
                     index=[pd.to_datetime('2000-01-01 01:00'),
                            pd.to_datetime('2000-01-01 02:00'),
                            pd.to_datetime('2000-01-01 03:00')],
                     columns=['A', 'B']
    )
    test_result = pd.DataFrame(
                     data=[[0.0, 0.0]],
                     index=[datetime.date(2000, 1, 1)],
                     columns=['A', 'B']
    )

    # Need to use Pandas testing functions to compare arrays
    pdt.assert_frame_equal(daily_mean(test_input), test_result)


def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers."""
    from catchment.models import daily_mean

    test_input = pd.DataFrame(
                     data=[[1, 2],
                           [3, 4],
                           [5, 6]],
                     index=[pd.to_datetime('2000-01-01 01:00'),
                            pd.to_datetime('2000-01-01 02:00'),
                            pd.to_datetime('2000-01-01 03:00')],
                     columns=['A', 'B']
    )
    test_result = pd.DataFrame(
                     data=[[3.0, 4.0]],
                     index=[datetime.date(2000, 1, 1)],
                     columns=['A', 'B']
    )

    # Need to use Pandas testing functions to compare arrays
    pdt.assert_frame_equal(daily_mean(test_input), test_result)


def test_daily_max_integers():
    """Test the daily max function for floats
    so you create an array as the test input
    then already create the right solution as the test_result
    so, when you run the test input with the function,
    the pytest will compare if the results from the function and the results you have from
    test_results are the same.


    """

    from catchment.models import daily_max
    test_input = pd.DataFrame(
        data=[[1.3, 2.3],
              [3.9, 4.2],
              [5.5, 6.2]],
        index=[pd.to_datetime('2000-01-01 01:00'),
               pd.to_datetime('2000-01-01 02:00'),
               pd.to_datetime('2000-01-01 03:00')],
        columns=['A', 'B']
    )
    test_result = pd.DataFrame(
        data=[[5.5, 6.2]],
        index=[datetime.date(2000, 1, 1)],
        columns=['A', 'B']
    )

        # Need to use Pandas testing functions to compare arrays
    pdt.assert_frame_equal(daily_max(test_input), test_result)
def test_daily_min_integers():
    """Test if the daily min function works for negatives
    so you create an array as the test input
    then already create the right solution as the test_result
    so, when you run the test input with the function,
    the pytest will compare if the results from the function and the results you have from
    test_results are the same.


    """

    from catchment.models import daily_min
    test_input = pd.DataFrame(
        data=[[-3.0, -3.9],
              [-9.7, -2.1],
              [-5.0, -6.2]],
        index=[pd.to_datetime('2000-01-01 01:00'),
               pd.to_datetime('2000-01-01 02:00'),
               pd.to_datetime('2000-01-01 03:00')],
        columns=['A', 'B']
    )
    test_result = pd.DataFrame(
        data=[[-9.7, -6.2]],
        index=[datetime.date(2000, 1, 1)],
        columns=['A', 'B']
    )

    # Need to use Pandas testing functions to compare arrays
    pdt.assert_frame_equal(daily_min(test_input), test_result)
