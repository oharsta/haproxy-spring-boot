package zilverline.lb;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.servlet.http.HttpServletRequest;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

@RestController
public class UserController {

    @GetMapping("/user")
    public Map<String, Long> user(HttpServletRequest request) {
        String name = String.class.cast(System.getProperties().get("server.name"));
        Map<String, Long> stats = Map.class.cast(request.getSession().getAttribute("stats"));
        if (stats == null) {
            stats = new ConcurrentHashMap<>();
            stats.put(name, 1L);
        } else {
            stats.compute(name, (key, previous) -> previous == null ? 1L : previous + 1);
        }
        request.getSession().setAttribute("stats", stats);
        return stats;
    }
}
