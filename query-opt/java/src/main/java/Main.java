import A4.Index;
import A4.KeySet;
import A4.Node;
import A4.PointerSet;

public class Main {
    public static void main(String[] args) throws Exception {
        Index expectedOutput = new Index(13);
        expectedOutput.nodes.set(0, new Node( // node #1
                new KeySet(new int[]{66, -1}),
                new PointerSet(new int[]{1, 2, 0})
        ));

        expectedOutput.nodes.set(1, new Node( // node #2
                new KeySet(new int[]{42, -1}),
                new PointerSet(new int[]{4, 5, 0})
        ));

        expectedOutput.nodes.set(2, new Node( // node #3
                new KeySet(new int[]{68, -1}),
                new PointerSet(new int[]{7, 8, 0})
        ));

        expectedOutput.nodes.set(4, new Node( // node #5
                new KeySet(new int[]{7, -1}),
                new PointerSet(new int[]{0, 0, 5})
        ));

        expectedOutput.nodes.set(5, new Node( // node #6
                new KeySet(new int[]{42, -1}),
                new PointerSet(new int[]{0, 0, 7})
        ));

        expectedOutput.nodes.set(7, new Node( // node #8
                new KeySet(new int[]{66, -1}),
                new PointerSet(new int[]{0, 0, 8})
        ));

        expectedOutput.nodes.set(8, new Node( // node #9
                new KeySet(new int[]{68, 99}),
                new PointerSet(new int[]{0, 0, 0})
        ));
        System.out.println("dfg");
    }
}
