import java.io.BufferedReader;
import java.io.InputStreamReader;

public class 단어_뒤집기2_17413_실버3 {
    public static String reverse(String word)
    {
        StringBuilder reversed = new StringBuilder();
        for(int i = word.length()-1; i >= 0; i--)
        {
            reversed.append(word.charAt(i));
        }
        return reversed.toString();
    }

    public static void main(String[] args) throws Exception
    {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String target = reader.readLine();

        StringBuilder result = new StringBuilder();

        boolean inTag = false; // 현재 태그 안의 문자를 받고 있는지 여부
        StringBuilder word = new StringBuilder(); // 현재 받고 있는 단어

        for(int i = 0; i < target.length(); i++)
        {
            char c = target.charAt(i);
            if(c == '<')
            {
                if(word.length() != 0)
                {
                    result.append(reverse(word.toString()));
                    word.setLength(0);
                }
                result.append(c);
                inTag = true;
            }
            else if(c == '>')
            {
                result.append(c);
                inTag = false;
            }
            else if(inTag)
            {
                result.append(c);
            }
            else if(c == ' ')
            {
                if(word.length() != 0)
                {
                    result.append(reverse(word.toString()));
                    word.setLength(0);
                }
                result.append(c);
            }
            else
            {
                word.append(c);
            }

            if(i == target.length()-1 && word.length() != 0)
            {
                result.append(reverse(word.toString()));
            }
        }

        System.out.printf(result.toString());
    }