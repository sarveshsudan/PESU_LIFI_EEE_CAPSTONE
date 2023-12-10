gltf = GLTF();
gltf.load('D:\pesu\7TH Sem from Oct\aebplugfortest.gltf');

vertices = gltf.geometry(1).vertices;
faces = gltf.geometry(1).faces;
normals = gltf.geometry(1).normals;

figure;
trisurf(faces, vertices(:, 1), vertices(:, 2), vertices(:, 3), ...
        'FaceColor', [0.8 0.8 0.8], 'EdgeColor', 'none');
axis equal;
xlabel('X');
ylabel('Y');
zlabel('Z');
