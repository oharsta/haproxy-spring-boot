package zilverline.lb;

import org.junit.Test;
import org.springframework.mock.web.MockHttpServletRequest;

import javax.servlet.http.HttpSession;
import java.util.Map;
import java.util.stream.IntStream;

import static org.junit.Assert.*;

public class UserControllerTest {

    private UserController subject = new UserController();

    @Test
    public void user() {
        MockHttpServletRequest request = new MockHttpServletRequest();
        System.getProperties().put("server.name", "app1");

        IntStream.range(0, 10).forEach(i ->subject.user(request));

        HttpSession session = request.getSession();
        Map<String, Long> stats = Map.class.cast(session.getAttribute("stats"));
        assertEquals(10L, Long.class.cast(stats.get("app1")).longValue());
    }
}