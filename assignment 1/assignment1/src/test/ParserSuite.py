import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):

    def test_201(self):
        """
        successful test series
        """
        input_text = """class Test {
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 201))

    def test_202(self):
        """
        successful test series
        """
        input_text = """class Test {
            int a;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 202))

    def test_203(self):
        """
        successful test series
        """
        input_text = """class Test {
            int a = "addmaximum",b = 0001.18;
            void aneue,onichann= 1213;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 203))

    def test_204(self):
        """
        successful test series
        """
        input_text = """class Test {
            int a = "addmaximum",b = 0001.18;
            static void aneue,onichann= 1213;
            void innuedo() {
            
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 204))



    def test_205(self):
        """
        successful test series
        """
        input_text = """class Test {
            int a = "addmaximum",b = 0001.18;
            static void aneue,onichann= 1213;
            void innuedo() {
            }
            Shape(float radius,width){
                             this.length := length;
                          this.width := width;
                 }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 205))

    def test_206(self):
        """
        successful test series
        """
        input_text = """class Test {
            static final int a = "addmaximum",b = 0001.18;
            static void aneue,onichann= 1213;
            void innuedo() {
                final int a = "addmaximum",b = 0001.18;
                void aneue,onichann= 1213;
            }
            Shape(float radius,width){
                             this.length := length;
                          this.width := width;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 206))

    def test_207(self):
        """
        successful test series
        """
        input_text = """class Test {
            static final int a = "addmaximum",b = 0001.18;
            static void aneue,onichann= 1213;
            void innuedo() {
                final int a = "addmaximum",b = 0001.18;
                void aneue,onichann= 1213;
                a := shiethole;
            }
            Shape(float radius,width){
                             this.length := length;
                          this.width := width;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 207))

    def test_208(self):
        """
        successful test series
        """
        input_text = """class Test {
                static final int a = "addmaximum",b = 0001.18;
                # static void aneue,onichann= {1,abc,sadf,0.0e25};
                void innuedo() {
                    final int a = "addmaximum",b = 0001.18;
                    # final testical = {1,"abc",3,0.0e25};
                    final testical notadipshit = {1,"abc",3,0.0e25};
                    void aneue,onichann = 1213;
                    a := shiethole;
                }
                Shape(float radius,width){
                                 this.length := length;
                              this.width := width;
                }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 208))

    def test_209(self):
        """
        successful test series
        """
        input_text = """class Test {
                static final int a = "addmaximum",b = 0001.18;
                final static int a = "addmaximum",b = 0001.18;
                # static void aneue,onichann= {1,abc,sadf,0.0e25};
                void innuedo() {
                    final int a = "addmaximum",b = 0001.18;
                    # final testical = {1,"abc",3,0.0e25};
                    int[10] testical = {1,"abc",3,0.0e25};
                    void aneue,onichann = 1213;
                    a := shiethole;
                }
                Shape(float radius,width){
                    this.length := length;
                    this.width := width;
                }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 209))

    def test_210(self):
        """
        successful test series
        """
        input_text = """
            class foo {
                type[7857] n = this.Shape(x.foo(5)[4]*(!m) + (s >= m || m+-n));
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 210))

    def test_211(self):
        """
        successful test series
        """
        input_text = """
            class foo {
                H[5] function(A a,b,c; H n){
                    (5+6).adopt := method.avocation(nein,nein,nein);
                }
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 211))

    def test_212(self):
        """
        successful test series
        """
        input_text = """
            class foo {
                H[5] function(A a,b,c; H n){
                    (5+6).adopt := ((((((((1))))))));
                }
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 212))

    def test_213(self):
        """
        successful test series
        """
        input_text = """class foo { H[5] function(A a,b,c; H n){ (x.foo(5)[4]*(!m) + (s >= m || m+-n)).adopt := 
        a.b.c(x.foo(5)[4]*(!m) + (s >= m || m+-n),x.foo(5)[4]*(!m) + (s >= m || m+-n)).b.c.a; } } """
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 213))

    def test_214(self):
        """
        successful test series
        """
        input_text = """class foo { H[5] function(A a,b,c; H n){ (x.foo(5)[4]*(!m) + (s >= m || m+-n))[1].adopt := 
        a.b.c(x.foo(5)[4]*(!m) + (s >= m || m+-n),x.foo(5)[4]*(!m) + (s >= m || m+-n)).b.c.a; } } """
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 214))

    def test_215(self):
        """
        successful test series
        """
        input_text = """class foo { H[5] function(A a,b,c; H n){ (x.foo(5)[4]*(!m) + (s >= m || m+-n))[x.foo(5)[4]*(
        !m) + (s >= m || m+-n)].adopt[x.foo(5)[4]*(!m) + (s >= m || m+-n).asdfadf] := a.b.c(x.foo(5)[4]*(!m) + (s >= 
        m || m+-n),x.foo(5)[4]*(!m) + (s >= m || m+-n)).b.c.a; 
                
                
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 215))

    def test_216(self):
        """
        error test series
        """
        input_text = """class foo { H[5] function(A a,b,c; H n){ (x.foo(5)[4]*(!m) + (s >= m || m+-n))[x.foo(5)[4]*(
        !m) + (s >= m || m+-n)].adopt[x.foo(5)[4]*(!m) + (s >= m || m+-n).asdfadf.b[12].a.c] := exp; # test fail 
        a.b.c.d } } """
        expect = "Error on line 3 col 16: }"
        self.assertTrue(TestParser.test(input_text, expect, 216))

    def test_217(self):
        """
        successful test series
        """
        input_text = """
        class Example2 extends ABC {
            float length,width;
            float getArea() {}
            Shape(float length,width){
            this.length := length;
            this.width := width;
            }
            void main(){
                s := new Rectangle(3,4);
                io.writeFloatLn(s.getArea());
                s := new Triangle(3,4);
                io.writeFloatLn(s.getArea());
            }
        } 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 217))

    def test_218(self):
        """
        successful series
        """
        input_text = """class Example2 extends ABC { void main(){ for x := (s >= m || m+-n).adopt[x.foo(5)[4]*(!m)] + 
        (s >= m || m+-n).asdfadf.b[12].a.c to (s >= m || m+-n).adoptx.foo(5)[4]*(!m) + (s >= m || m+-n).asdfadf.b[
        12].a.c do { io.writeIntLn(x); } } } """
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 218))

    def test_219(self):
        """
        successful series
        """
        input_text = """
        class Example2 extends ABC {
            void main(){
                for x := (1) to 2 do
                    io.writeIntLn(x);
            }
        } 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 219))

    def test_220(self):
        """
        successful series
        """
        input_text = """
        class Example2 extends ABC {
            void main(){
                for x := ((((0||1)))) to something_big do
                    for x := ((((0||1)))) to something_big do
                        for x := ((((0||1)))) to something_big do
                            for x := ((((0||1)))) to something_big do
                                a:=1;
            }
        } 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 220))

    def test_221(self):
        """
        successful series
        """
        input_text = """
        class Example2 extends ABC {
            void main(){
                break;
            }
        } 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 221))

    def test_222(self):
        """
        successful series
        """
        input_text = """
        class Example2 extends ABC {
            void main(){
                continue;
            }
        } 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 222))

    def test_223(self):
        """
        successful series
        """
        input_text = """
        class Example2 extends ABC {
            void main(){
                return ((((0||1))));
            }
        } 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 223))

    def test_224(self):
        """
        successful series
        """
        input_text = """
        class Example2 extends ABC {
            void main(){
                if flag then
                    io.writeStrLn("Expression is true");
                else
                    io.writeStrLn ("Expression is false");
            }
        } 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 224))

    def test_225(self):
        """
        successful series
        """
        input_text = """
        class Example2 extends ABC {
            void main(){
                if flag then
                    for x := ((((0||1)))) to something_big do
                    for x := ((((0||1)))) to something_big do
                        for x := ((((0||1)))) to something_big do
                            for x := ((((0||1)))) to something_big do
                                a:=1;
                else
                    io.writeStrLn ("Expression is false");
            }
        } 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 225))

    def test_226(self):
        """
        successful series
        """
        input_text = """
        class Example2 extends ABC {
            void main(){
                if flag then
                    for x := ((((0||1)))) to something_big do
                    for x := ((((0||1)))) to something_big do
                        for x := ((((0||1)))) to something_big do
                            for x := ((((0||1)))) to something_big do
                                a:=1;
                else
                    io.writeStrLn ("Expression is false");
            }
        } 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 226))

    def test_227(self):
        """
        error series
        """
        input_text = """
        class MyFooClass {
                        string s ="huhuhu", l = true;
                        int[5] cam(){int a,b;}
                        foo;
        }
        """
        expect = "Error on line 5 col 27: ;"
        self.assertTrue(TestParser.test(input_text, expect, 227))

    def test_228(self):
        """
        error series
        """
        input_text = """
        class ID {
                        string name;
                        ID(){
                            this.name := nil;
                        }
                    };
                    class ID{
                        int a;
                    }

        """
        expect = "Error on line 7 col 21: ;"
        self.assertTrue(TestParser.test(input_text, expect, 228))

    def test_229(self):
        """
        error series
        """
        input_text = """
        class a{
            int b(){
            (b[1]).c.a(6) := new a()+5;
            a.b();
            a[3+x.foo(2)] := a[b[2]] +3;
            }
        }
        """
        expect = "Error on line 4 col 26: :="
        self.assertTrue(TestParser.test(input_text, expect, 229))

    def test_230(self):
        """
        error series
        """
        input_text = """
        class program {
            void a(){
                (this.b[3]).c.foo().big() := 3* foo(a, b);
            } 
        }
        """
        expect = "Error on line 4 col 42: :="
        self.assertTrue(TestParser.test(input_text, expect, 230))

    def test_231(self):
        """
        successful series
        """
        input_text = """
        class a{
            int get() {
                cfefer := ferb[35 - foo(2)];
                return k.y();
            }
            int get() {

                return kfer.y();
            }
            int get() {
                ferfec := b[35 - foo(2)];
                return tgrk.rfey();
            }
        }
        """
        expect = "Error on line 4 col 39: ("
        self.assertTrue(TestParser.test(input_text, expect, 231))

    def test_232(self):
        """
        successful series
        """
        input_text = """
        class Example2 extends ABC {
            Ab[5] n = this.hocLai(x.foo(5)[4]*(!m) + (s >= m || m+-n));
            void main(){
            int m = h;
            float c;
            a := 4;
            s.shape();
            }
        } 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 232))

    def test_233(self):
        """
        successful series
        """
        input_text = """
        class A {
            int get() {
                a[4 + noope.foo(2)] := 2;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 233))

    def test_234(self):
        """
        error series
        """
        input_text = """
        class A {
            int get() {
            /*
                a[4 + noope.foo(2)] := 2;
            }
        }
        """
        expect = "Error on line 4 col 12: /"
        self.assertTrue(TestParser.test(input_text, expect, 234))

    def test_235(self):
        """
        successful series
        """
        input_text = """
        class A {
            /*
            int get() {
                a[4 + noope.foo(2)] := 2;
            }
            */
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 235))

    def test_236(self):
        """
        error series
        """
        input_text = """
        class A {
            int get() {
            /*
                a[4 + noope.foo(2)] := 2;
            }
            */
        }
        """
        expect = "Error on line 9 col 8: <EOF>"
        self.assertTrue(TestParser.test(input_text, expect, 236))

    def test_237(self):
        """
        error series
        """
        input_text = """
        class A {
            Ab[5] n = this.hocLai(x.foo(5)[4]*(!m) + (s >= m || m+-n));
            H[5] hocPhi(A a,b,c; H n){
                int m = h;
                int b, h = 40, k, d = {3,true,false,5.e5,5.8e+12};
                a := 4;
                s.shape();
                float c;
            }
        }
        """
        expect = "Error on line 9 col 16: float"
        self.assertTrue(TestParser.test(input_text, expect, 237))
        
    def test_238(self):
        """
        successful series
        """
        input_text = """class A {
            int get() {
                foo := -8;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 238))

    def test_239(self):
        """
        successful series
        """
        input_text = """class A {
            HailHitler() {
                c := 6 <=9;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 239))

    def test_240(self):
        """
        successful series
        """
        input_text = """class A {
            int get() {
                a := 2 % 3;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 240))

    def test_241(self):
        """
        successful series
        """
        input_text = """class A {
            int get() {
                a := !b;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 241))

    def test_242(self):
        """
        successful series
        """
        input_text = """class A {
            int get() {
                a[4] := 2;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 242))

    def test_243(self):
        """
        successful series
        """
        input_text = """class A {
            int get() {
                a[4+3] := 2 || 3;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 243))

    def test_244(self):
        """
        successful series
        """
        input_text = """class A {
            int dasdfasdf() {
                a[4 + subboi.foo(2)] := ((((((1||2||3))))));
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 244))

    def test_245(self):
        """
        successful series
        """
        input_text = """class a {
                float main() {
                    whatdidyousaytome.me(1*2\\5);
                }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 245))

    def test_246(self):
        """
        successful series
        """
        input_text = """class a {
                    void main() {
                        io.foandbar(1/2/2);
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 246))

    def test_247(self):
        """
                successful series
        """
        input_text = """class a {
                    int main() {
                        io.writeFloat(1-1*3++2*h\\i);
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 247))

    def test_248(self):
        """
        successful series
        """
        input_text = """class A {
            int get() {
                c := 6 <= (((((9)))));
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 248))

    def test_249(self):
        """
        error series
        """
        input_text = """
        class A {
            int get() {
                6.foo(7);
            }
        }
        """
        expect = "Error on line 4 col 18: foo"
        self.assertTrue(TestParser.test(input_text, expect, 249))

    def test_250(self):
        """
        successful series
        """
        input_text = """
        class A {
            int get() {
                this.nothing_to_return();   /* call method */
                return {12, 4} * "ad" + 14 ---- 12 + !!!!!!!!!!!!(!!3) % arr["b"];
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 250))

    def test_251(self):
        """
        error series
        """
        input_text = """
        class Shape {
            float length,width;
            float getArea() {}
            Shape(float length,width){
                this.length := "length";
                this.width := width;
                return;
                return;
                return;
                if flag then
                    for x := ((((0||1)))) to something_big do
                    for x := ((((0||1)))) to something_big do
                        for x := ((((0||1)))) to something_big do
                            for x := ((((0||1)))) to something_big do
                                {
                                    a.foo();
                                }
                else
                    io.writeStrLn ("Expression is false");
            }
        }
        """
        expect = "Error on line 8 col 22: ;"
        self.assertTrue(TestParser.test(input_text, expect, 251))

    def test_252(self):
        """
        successful series
        """
        input_text = """
        class Shape {
        }
        class Rectangle extends Shape {
        }
        class Triangle extends Shape {
        }
        class Example2 {
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 252))

    def test_253(self):
        """
        successful series
        """
        input_text = """
        class Shape {
            float length,width;
            float getArea() {}
            Shape(float length,width){
                this.length := "length";
                this.width := width;
                return 1;
                return 2||2;
                return 3%3;
                if flag then
                    for x := ((((0||1)))) to something_big do
                    for x := ((((0||1)))) to something_big do
                        for x := ((((0||1)))) to something_big do
                            for x := !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1*((((0||1)))) to something_big do
                                {
                                    a.foo();
                                    for x := ((((0||1)))) to something_big do
                                        for x := ((((0||1)))) to something_big do
                                            for x := ((((0||1)))) to something_big do
                                                break;
                                }
                else
                    io.writeStrLn ("Expression is false");
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 253))

    def test_254(self):
        """
        successful series
        """
        input_text = """
        class Shape {
            static final float length,width;
            final static float length,width;
            static float getArea() {}
            Shape(float length,width){
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 254))

    def test_255(self):
        """
        successful series
        """
        input_text = """
        class Shape {
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 255))

    def test_256(self):
        input_text = """
        class 1Shape {
        }
        """
        expect = "Error on line 2 col 14: 1"
        self.assertTrue(TestParser.test(input_text, expect, 256))

    def test_257(self):
        input_text = """
        class sgrsdrfgsdfgsdfgsgsdfgsfg {
            final string a;
            dfasdfasdf(){
                this.b:=nil;
            }
        };
        """
        expect = "Error on line 7 col 9: ;"
        self.assertTrue(TestParser.test(input_text, expect, 257))

    def test_258(self):
        input_text = """
        class sgrsdrfgsdfgsdfgsgsdfgsfg {
            final string a;
            dfasdfasdf(){
                this.b:=nil;
            }
            dfasdfasdf(int adfasdfasdf = suckmyass){
            }
        }
        """
        expect = "Error on line 7 col 39: ="
        self.assertTrue(TestParser.test(input_text, expect, 258))

    def test_259(self):
        input_text = """
        class sgrsdrfgsdfgsdfgsgsdfgsfg {
            final string a;
            dfasdfasdf(){
                this.b=nil;
            }
        };
        """
        expect = "Error on line 5 col 22: ="
        self.assertTrue(TestParser.test(input_text, expect, 259))

    def test_260(self):
        """
        successful series
        """
        input_text = """
        class ID {
            static int total=0;
            string name;
            ID(){
                this.name:=nil;
            }
            ID(string name){
                this.name:=name;
                ID.total := ID.total +1;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 260))

    def test_261(self):
        """
        successful test series
        """
        input_text = """
        class program {
            int b = 2;
            int[5] a = {1, 2, 3, 4, 5};
            int c = b*a[0;
        }
        """
        expect = "Error on line 5 col 25: ;"
        self.assertTrue(TestParser.test(input_text, expect, 261))

    def test_262(self):
        """
        syntax error test series
        """
        input_text = """class QuotientRemainder {
                       static void main(string[2] args) {
                            5+5 := y;
                        }
                    }"""
        expect = "Error on line 3 col 29: +"
        self.assertTrue(TestParser.test(input_text, expect, 262))

    def test_263(self):
        """
        syntax error test series
        """
        input_text = """class Example1 {
                    int factorial(int n){ {}
                    int y = 20;
                    if n == 0 then return 1; else return n * this.factorial(n - 1);
                    }
                    void main(){
                    int x;
                    x := io.readInt();
                    io.writeIntLn(this.factorial(x));
                    }
                    }"""
        expect = "Error on line 3 col 20: int"
        self.assertTrue(TestParser.test(input_text, expect, 263))

    def test_264(self):
        """
        successful series
        """
        input_text = """class QuotientRemainder {
                        static void main(string[2] args) {

                            System.out.println("Quotient = " + quotient);
                            System.out.println("Remainder = " + remainder);
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 264))

    def test_265(self):
        input_text = """class Shape {
                        float length,width;
                        float getArea() {}
                        Shape(float length,width){
                            this.length := length;
                            this.width := width;
                        }
                    }
                    class Rectangle extends Shape {
                        float getArea(){
                            return this.length*this.width;
                        }
                    }
                    class Triangle extends Shape {
                        float getArea(){
                            return this.length*this.width / 2;
                        }
                    }
                    class Example2 {
                        void main(){
                            Exam[2] x = {1.2, 3.4, 5};
                            Shape s = new Rectangle(3,4);
                            io.writeFloatLn(s.getArea());
                            s := 2+3-95*74;
                            io.writeFloatLn(s.getArea());
                            y := {1.2 ,2, 3};
                            a > this.a.a := 5;
                            return a;
                        }
                    }"""
        expect = "Error on line 27 col 30: >"
        self.assertTrue(TestParser.test(input_text, expect, 265))

    def test266(self):
        input_text = """class SHap {
            int get() {
                a := b[3 - foo(2)];
            }
        }"""
        expect = "Error on line 3 col 30: ("
        self.assertTrue(TestParser.test(input_text, expect, 266))

    def test_267(self):
        """
        successful series
        """
        input_text = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 267))

    def test_268(self):
        input_text = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input_text, expect, 268))

    def test_269(self):
        input_text = """class { }"""
        expect = "Error on line 1 col 6: {"
        self.assertTrue(TestParser.test(input_text, expect, 269))

    def test_270(self):
        input_text = """class ABC }"""
        expect = "Error on line 1 col 10: }"
        self.assertTrue(TestParser.test(input_text, expect, 270))

    def test_271(self):
        """
        successful series
        """
        input_text = """class Shape {
                        static final int numOfShape = 0;
                        final int immuAttribute = 0;
                        float length,width;
                        static int getNumOfShape() {
                            return numOfShape;
                        }
                    }
                    class Rectangle extends Shape {
                        float getArea(){
                            return this.length*this.width;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 271))

    def test_272(self):
        """
        successful series
        """
        input_text = """class Shape {
                        static final int numOfShape = 0;
                        final int immuAttribute = 0;
                        float length,width;
                        static int getNumOfShape() {
                            return numOfShape;
                        }
                    }
                    class Rectangle extends Shape {
                        float getArea(){
                            return this.length*this.width;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 272))

    def test_273(self):
        """
        successful series
        """
        input_text = """class Example2 extends ABC {
                        int length,width;
                        float getArea() {}
                        Shape(float length,width){
                            this.length := length;
                            this.width := width;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 273))

    def test_274(self):
        """
        successful series
        """
        input_text = """class Example1 {
                        void main(){
                            int x;
                            l[3] := 2*value*2/2-c;
                            x := io.readInt();
                            io.writeIntLn(this.factorial(x));
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 274))

    def test_275(self):
        """
        successful series
        """
        input_text = """class Shape {
                        float length,width;
                        float getArea() {}
                        Shape(float length,width){
                            this.length := length;
                            this.width := width;
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 275))

    def test_276(self):
        input_text = """
        class simple{
            float x, y = 1e9;
            int[5] arr = {1.0e+5, 2e-9, true, "ab\\tc", false};
            Return;
        }
        """
        expect = "Error on line 5 col 18: ;"
        self.assertTrue(TestParser.test(input_text, expect, 276))

    def test_277(self):
        input_text = """
        class simple{
            final float x = "string \\"", y = 1e9;
            int[5] arr = {1.0e+5, 2e-9, ___, "ab\\tc", false};
        }
        """
        expect = "Error on line 4 col 40: ___"
        self.assertTrue(TestParser.test(input_text, expect, 277))

    def test_278(self):
        input_text = """
        class simple extends ABC {
            static final string = "string \\"", y = 1e9;
        }
        """
        expect = "Error on line 3 col 32: ="
        self.assertTrue(TestParser.test(input_text, expect, 278))

    def test_279(self):
        input_text = """
        class simple extends ABC {
            boolean final = "string \\"";
        }
        """
        expect = "Error on line 3 col 20: final"
        self.assertTrue(TestParser.test(input_text, expect, 279))

    def test_280(self):
        """
        success series
        """
        input_text = """
        class complex extends simple {
            boolean Final = "string \\"", y = 1e9;
            void nothing_to_return(){
                sys.print_some_thing();    
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 280))

    def test_281(self):
        """
        success series
        """
        input_text = """
        class complex extends simple {
            void nothing_to_return(){
                sys.print_some_thing();    
            }

            int main(){
                this.nothing_to_return();   /* call method */
                return x + 2*y;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 281))

    def test_282(self):
        input_text = """
        class complex extends simple {
            void nothing_to_return(){
                sys.print_some_thing();     # print some thing, i dont know\\n
            }

            void main(){
                this.nothing_to_return();   /* oh no, oh no, oh no no no no no*/*/
            }
        }
        """
        expect = "Error on line 8 col 80: *"
        self.assertTrue(TestParser.test(input_text, expect, 282))

    def test_283(self):
        """
        success series
        """
        input_text = """
        class Luxubu {
            final int main = "main";

            float main(int n; float m){
                if n == 0 then
                    return 1.;
                else
                    return n % sys.reduce(m);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 283))

    def test_284(self):
        input_text = """
        class Luxubu {
            final int main = "main";

            void foo(){
                # pass
            }

            float main(int n; float m, string str){
                if n == 0 then
                    return 1.;
                else
                    return n % sys.reduce(m);
            }
        }
        """
        expect = "Error on line 9 col 39: string"
        self.assertTrue(TestParser.test(input_text, expect, 284))

    def test_285(self):
        input_text = """
        class Luxubu {
            static int main = "main";
            void main(){
                if sys.flag then
                    this.foo(n, n*m);
                else
                    /*/*/* pass */
            }
        }
        """
        expect = "Error on line 8 col 25: *"
        self.assertTrue(TestParser.test(input_text, expect, 285))

    def test285(self):
        input_text = """
        class Extends {
            static int Main(string args){
                {
                    final string str = args[0];
                    if str then break;
                }
            }

            boolean main(string args, kwargs){     # class type
                else if args[0] == kwargs[0] then
                return true;
                return false;
            }
        }
        """
        expect = "Error on line 11 col 16: else"
        self.assertTrue(TestParser.test(input_text, expect, 285))

    def test286(self):
        input_text = """
        class main extends Main {
            void nothing(){
                # really nothing :V
            }
            static string main(){
                str := "1" + "1";
                cls.f(1 >= 4) + cls.g(cls.f(cls.a("a", "af")));
                return str ^ "= \\"2\\"";
            }
        }
        """
        expect = "Error on line 8 col 30: +"
        self.assertTrue(TestParser.test(input_text, expect, 286))

    def test287(self):
        """
        success series
        """
        input_text = """
        class fasdfasdfasdf {
            static int main = "main";

            float foo(int n; float m, String){
                if n == 0 then
                    return 1.;
                else
                    return n % sys.reduce(m);
            }

            void main(){
                if sys.flag then
                    this.foo(n, n*m);
                else
                {{
                    c := "akf"[0] + x[{1,2, 4}];
                    sys.print(c);
                }}
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 287))

    def test288(self):
        """
        success series
        """
        input_text = """
        class complex extends simple {
            void nothing_to_return(){
                sys.print_some_thing();     # print some thing, i dont know
            }

            int main(){
                this.nothing_to_return();   /* call method */
                return {12, 4} * "ad" + 14 ---- 12 + !!!!!!!!!!!!(!!3) % arr["b"];
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 288))

    def test289(self):
        input_text = """
        class complex extends simple {
            void nothing_to_return(){
                c := sys.count(/*/*DDDDDD*/) * sys.f(214);
            }

            int main(){
                this.nothing_to_return();   /* call method */
                a := {12, 4} * "ad" + 14 ---- 12 + !!!!!!!!!!!!(!!3) % arr["b" - 97];

                return {12, 4}[1];       #   ----> successful or not <----
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 289))

    def test290(self):
        input_text = """
        class Calculation{
            int cal(){
                int[10] arr = {0.};
                for i := 0 to y do
                {
                    {
                        # just a comment
                        kk := 123;
                        123 := kk;
                    }
                    io.writeln(i);
                }
            }
        }
        """
        expect = "Error on line 10 col 28: :="
        self.assertTrue(TestParser.test(input_text, expect, 290))

    def test_291(self):
        input_text = """
        class main extends Main {
            int count = 0;

            void method(){
                sys.a.b.c().d.e.a.c.b().f(a, b, sys.b);
                int a = 0;
            }
        }
        """
        expect = "Error on line 6 col 54: ;"
        self.assertTrue(TestParser.test(input_text, expect, 291))

    def test292(self):
        input_text = """
        class Main extends ABC{
            float a = ----1234 || +++++++False + -+-+ 22222;

            void main(){
                b := {{{{}}}, {123}};
            }
        }
        """
        expect = "Error on line 6 col 22: {"
        self.assertTrue(TestParser.test(input_text, expect, 292))

    def test293(self):
        input_text = """
        class Add extends Operator{
            int main(){
                {
                    sys.print("s = ", this.accumulated(0, 10, 2e-3));
                }
                {
                    int a = (5 + this.f() * 3 + arr[10]) * 5 \\ 8;
                    b := "123" * "123" , - 2 == "sss";
                    return a ^ b;
                }
            }
        }
        """
        expect = "Error on line 9 col 39: ,"
        self.assertTrue(TestParser.test(input_text, expect, 293))

    def test294(self):
        input_text = """
        class complex extends simple {
            void nothing_to_return(){
                sys.print_some_thing();     # print some thing, i dont know
            }

            int main(){
                this.nothing_to_return();   /* call method */
                inp := ppapa[/**4235 dasfj dd 44 **/ this.g(-----------/*/*-----*/----------------this.f())];
                x := "adf" * {q23, 4, "af"}[Return 45;];
                return x * inp;
            }
        }
        """
        expect = "Error on line 10 col 30: q23"
        self.assertTrue(TestParser.test(input_text, expect, 294))

    def test295(self):
        input_text = """
        class ABC extends DEF{
            void method(){
                if "" then
                if 1 then
                    inp := f23 + ads[2:10] +  ++++ 2 *f /* "87235jkfgshgsfg $&^# */ ;
                else return 0;
            }
        }
        """
        expect = "Error on line 6 col 38: :"
        self.assertTrue(TestParser.test(input_text, expect, 295))

    def test296(self):
        input_text = """
        class ABC extends DEF{
            void method(){
                if "" then
                if 1 then
                    inp := [234]fsfsg + 13 \\. 124;
                else return 0;
            }
        }
        """
        expect = "Error on line 6 col 27: ["
        self.assertTrue(TestParser.test(input_text, expect, 296))

    def test297(self):
        """
        successful test series
        """
        input_text = """
        class ABC extends DEF{
            void method(){
                if "" then
                in := 123 - 4234 +- 432 || !False;
                inp := {123, 435, 423} * in;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 297))

    def test298(self):
        input_text = """
        class Main extends ABC{
            static int i = x[true] + 5;
            int[true] arr = {"Qua Deo Ngang", "Ba Huyen Thanh Quan"};

            static float main(string args){
                sys.param_x() := 1234 || False + 22222;
                return sys.param_x;
            }
        }
        """
        expect = "Error on line 4 col 16: true"
        self.assertTrue(TestParser.test(input_text, expect, 298))

    def test299(self):
        input_text = """
        class Add extends Operator {
            int accumulated(int init; int n, step){
                int s = init;
                for i := 0 to n do
                    s := s + step;
                return sys.to_string(s, reverse==true);
            }

            class main extends Main {
                static int count = 0;
            }
        }
        """
        expect = "Error on line 10 col 12: class"
        self.assertTrue(TestParser.test(input_text, expect, 299))

    def test_300(self):
        """
        successful test series
        """
        input_text = """class Test {
            int a = "addmaximum",b = 0001.18;
            static void aneue,onichann= 1213;
            void innuedo() {

            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 300))


    '''
    def test_(self):
        """
        successful series 
        """
        input_text = """
        class Example2 extends ABC {
            void main(){
                
            }
        } 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, ))
    def test_(self):
        """
        error series 
        """
        input_text = """
        class Example2 extends ABC {
            void main(){
                
            }
        } 
        """
        expect = ""
        self.assertTrue(TestParser.test(input_text, expect, ))
    '''

