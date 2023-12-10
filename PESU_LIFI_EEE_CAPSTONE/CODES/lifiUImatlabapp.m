classdef digiapptest < matlab.apps.AppBase

    properties (Access = private)
        UIFigure      matlab.ui.Figure
        Axes          matlab.ui.control.UIAxes
        LoadButton    matlab.ui.control.Button
        Image         matlab.graphics.primitive.Image
    end

    methods (Access = private)

        function startupFcn(app)

            defaultImage = imread('D:\pesu\7TH Sem from Oct\digi.jpg');
            app.Image = imagesc(app.Axes, defaultImage);

            app.Axes.ButtonDownFcn = @app.axesClick;
        end

        function LoadButtonPushed(app, ~)
    
            [file, path] = uigetfile({'*.jpg;*.jpeg', 'JPEG Files (*.jpg, *.jpeg)'; '*.png', 'PNG Files (*.png)'}, 'Select an Image File');
            if isequal(file, 0)
             
                return;
            end

            imagePath = fullfile(path, file);
            imageData = imread(imagePath);
            app.Image.CData = imageData;

            app.Axes.ButtonDownFcn = @app.axesClick;
        end

        function axesClick(app, ~, event)

            clickPosition = event.IntersectionPoint(1:2);

            imageSize = size(app.Image.CData);
            imageWidth = imageSize(2);
            clickX = clickPosition(1);

            if clickX <= imageWidth / 2
                sendData(app, 'left');
            else
                sendData(app, 'right');
            end
        end

        function sendData(app, data)

            RaspberryPi_IP = '10.14.146.67';
            RaspberryPi_Port = 12345;

            tcpClient = tcpclient(RaspberryPi_IP, RaspberryPi_Port);

            try

                write(tcpClient, data);

                disp(['Data sent successfully: ' data]);

            catch ME
                disp(['Error: ' ME.message]);

            end

            close(tcpClient);
        end
    end

    methods (Access = public)

        function app = YourApp

            createComponents(app);

            registerApp(app, app.UIFigure);

            runStartupFcn(app, @startupFcn);

            if nargout == 0
                clear app;
            end
        end

        function delete(app)

            delete(app.UIFigure);
        end
    end
end
