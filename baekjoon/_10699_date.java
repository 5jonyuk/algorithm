import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

public class _10699_date {
    public static void main(String[] args) {
        LocalDate today = LocalDate.now();
        System.out.println(today.format(DateTimeFormatter.ofPattern("yyyy-MM-dd")));
    }
}
