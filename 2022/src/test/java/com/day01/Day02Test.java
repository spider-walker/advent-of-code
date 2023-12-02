package com.day01;


import org.junit.jupiter.api.DisplayName;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Order;
import org.junit.jupiter.api.Test;
@DisplayName("Day 02")
class Day02Test {
    String sample ="input/day02/path-01/sample.txt";
    String input ="input/day02/path-01/input.txt";

    Day02 day=new Day02();
    @DisplayName("Path 01: Sample")
    @Test
    @Order(1)
    void samplePath01() {
        long answer = day.path01(sample);
        assertEquals(24000, answer);

    }
    @DisplayName("Path 01: Real")
    @Test
    @Order(2)
    void inputPath01() {
        long answer = day.path01(input);
        assertEquals(74394, answer);

    }

    @DisplayName("Path 02: Sample")
    @Test
    @Order(1)
    void samplePath02() {
        Long []answer = day.path02(sample);
        assertEquals(24000, answer[0]);
        assertEquals(11000, answer[1]);
        assertEquals(10000, answer[2]);

    }
    @DisplayName("Path 02: Real")
    @Test
    @Order(2)
    void inputPath02() {
        Long []answer = day.path02(input);
        assertEquals(74394, answer[0]);
        assertEquals(69863, answer[1]);
        assertEquals(68579, answer[2]);
        assertEquals(68579+74394+69863, answer[1]+answer[0]+answer[2]);

    }
}