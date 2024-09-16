package com.spiderwalker.aoc;

import static org.junit.Assert.assertTrue;

import java.util.Arrays;
import java.util.List;

import org.junit.Test;

public class Day10Test {
    Day10 day10 = new Day10();

    @Test
    public void shouldAnswerWithTrue() {
        List<String> lines = day10.readFile("sample.txt");
        assertTrue(lines.size() > 0);
         char[] s = day10.findS(lines);
         
        System.err.println("XXX:"+ Arrays.toString(s));

    }
}