package com.day01;


import org.junit.jupiter.api.DisplayName;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Order;
import org.junit.jupiter.api.Test;

@DisplayName("Day 01")
class Day01Test {
    Day01 day01Path01=new Day01();
    @DisplayName("Path 01: Sample")
    @Test
    @Order(1)
    void samplePath01() {
        String file ="input/day01/path-01/sample.txt";
        long answer = day01Path01.path01(file);
        assertEquals(24000, answer);

    }
    @DisplayName("Path 01: Real")
    @Test
    @Order(2)
    void inputPath01() {
        String file ="input/day01/path-01/input.txt";
        long answer = day01Path01.path01(file);
        assertEquals(74394, answer);

    }

    @DisplayName("Path 02: Sample")
    @Test
    @Order(1)
    void samplePath02() {
        String file ="input/day01/path-01/sample.txt";
        Long []answer = day01Path01.path02(file);
        assertEquals(24000, answer[0]);
        assertEquals(11000, answer[1]);
        assertEquals(10000, answer[2]);

       }
    @DisplayName("Path 02: Real")
    @Test
    @Order(2)
    void inputPath02() {
        String file ="input/day01/path-01/input.txt";
        Long []answer = day01Path01.path02(file);
        assertEquals(74394, answer[0]);
        assertEquals(69863, answer[1]);
        assertEquals(68579, answer[2]);
        assertEquals(68579+74394+69863, answer[1]+answer[0]+answer[2]);

    }
}