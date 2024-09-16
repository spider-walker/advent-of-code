package com.spiderwalker.aoc;

import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

public class Day10 {

    public List<String> readFile(String fileName) {
        try {

            return Files.readAllLines(Paths.get(fileName));
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }

    public char[] findS(List<String> lines) {
        int k = 0;
        for (String line : lines) {
            if (line.contains("S")) {
                k++;
            }
        }

        int x = lines.get(k).indexOf("S");

        return new char[] { lines.get(k).charAt(x + 1), lines.get(k + 1).charAt(x), lines.get(k).charAt(x - 1),
                lines.get(k - 1).charAt(x) };
    }

}
