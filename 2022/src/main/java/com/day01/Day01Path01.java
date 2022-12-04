package com.day01;

import java.io.File;
import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.util.List;

public class Day01Path01 {
    public static void main(String[] args) {
        try {
            List<String> list = Files.readAllLines(new File("input/day01/path-01/input.txt").toPath(), Charset.defaultCharset());
            long []highest = new long[3];
            long currentSum = 0;
            for (String s : list) {
                if (s.trim().length() == 0) {
                    if (currentSum>= highest[0]) {
                        highest[0] = currentSum;
                    }

                    if (currentSum>= highest[1]) {
                        highest[1] = currentSum;
                    }
                    if (currentSum>= highest[2]) {
                        highest[1] = currentSum;
                    }
                    currentSum = 0;

                } else {
                    currentSum += Long.parseLong(s);
                }
            }
            System.out.println(highest[0]);
            System.out.println(highest[1]);
            System.out.println(highest[2]);

        } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }

    }
}
