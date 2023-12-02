package com.day01;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.io.File;
import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

public class Day02 {
    private static Logger LOGGER = LogManager.getLogger(Day02.class);

    public long path01(String file) {
        long currentSum = 0;
        long highest = 0;
        try {
            List<String> list = Files.readAllLines(new File(file).toPath(), Charset.defaultCharset());
            for (String s : list) {
                if (s.trim().length() == 0) {
                    if (currentSum > highest) {
                        highest = currentSum;
                    }
                    currentSum = 0;

                } else {
                    currentSum += Long.parseLong(s);
                }
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

        return highest;
    }

    public Long[] path02(String file) {
        long currentSum = 0;
        List<Long> longs = new ArrayList<>();
        try {
            List<String> list = Files.readAllLines(new File(file).toPath(), Charset.defaultCharset());
            for (String s : list) {
                if (s.trim().length() == 0) {
                    longs.add(currentSum);
                    currentSum = 0;
                } else {
                    currentSum += Long.parseLong(s);
                }
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        LOGGER.info(longs);


        return longs.stream().sorted(Comparator.reverseOrder()).collect(Collectors.toList()).toArray(new Long[0]);
    }


}
