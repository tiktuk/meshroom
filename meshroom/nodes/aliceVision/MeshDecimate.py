from meshroom.core import desc

class MeshDecimate(desc.CommandLineNode):
    internalFolder = '{cache}/{nodeType}/{uid0}/'
    commandLine = 'aliceVision_meshDecimate {allParams}'

    cpu = desc.Level.NORMAL
    ram = desc.Level.NORMAL

    inputs = [
        desc.File(
            name="input",
            label='Input Mesh (OBJ file format).',
            description='',
            value='',
            uid=[0],
            ),
        desc.FloatParam(
            name='simplificationFactor',
            label='Simplification factor',
            description='Simplification factor',
            value=0.5,
            range=(0.0, 1.0, 0.01),
            uid=[0],
        ),
        desc.IntParam(
            name='nbVertices',
            label='Fixed Number of Vertices',
            description='Fixed number of output vertices.',
            value=0,
            range=(0, 1000000, 1),
            uid=[0],
        ),
        desc.IntParam(
            name='minVertices',
            label='Min Vertices',
            description='Min number of output vertices.',
            value=0,
            range=(0, 1000000, 1),
            uid=[0],
        ),
        desc.IntParam(
            name='maxVertices',
            label='Max Vertices',
            description='Max number of output vertices.',
            value=0,
            range=(0, 1000000, 1),
            uid=[0],
        ),
        desc.BoolParam(
            name='flipNormals',
            label='Flip Normals',
            description='Option to flip face normals.\n'
                        'It can be needed as it depends on the vertices order in triangles\n'
                        'and the convention change from one software to another.',
            value=False,
            uid=[0],
        ),
        desc.ChoiceParam(
            name='verboseLevel',
            label='Verbose Level',
            description='''verbosity level (fatal, error, warning, info, debug, trace).''',
            value='info',
            values=['fatal', 'error', 'warning', 'info', 'debug', 'trace'],
            exclusive=True,
            uid=[],
        ),
    ]

    outputs = [
        desc.File(
            name="output",
            label="Output mesh",
            description="Output mesh (OBJ file format).",
            value='{cache}/{nodeType}/{uid0}/mesh.obj',
            uid=[],
            ),
    ]
