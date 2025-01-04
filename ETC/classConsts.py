class Hello:
    HELLO = 10
    def hello(self):
        for _ in range(Hello.HELLO):
            print("Hello, Ahmed")


hello = Hello()

hello.hello()